import pytest
from app.database import Base
from app.models import Event, EventTitle, EventDescription, EventLocation


def test_health(client):
    resp = client.get("/api/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "version" in data


class TestEventsCRUD:
    def _create_event_payload(self, suffix=""):
        return {
            "date": "2020-01-01",
            "date_precision": "day",
            "category": "politics",
            "tags": ["test", f"tag{suffix}"],
            "importance": 80,
            "titles": [
                {"language": "en", "title": f"Test Event{suffix}"},
                {"language": "zh_tw", "title": f"測試事件{suffix}"},
            ],
            "descriptions": [
                {
                    "language": "en",
                    "summary": f"Summary{suffix}",
                    "content": f"Content{suffix}",
                }
            ],
            "location": {
                "lat": 39.9,
                "lng": 116.4,
                "country": "CN",
                "names": {"en": "Beijing", "zh_tw": "北京"},
            },
        }

    def test_create_event(self, client):
        resp = client.post("/api/events", json=self._create_event_payload())
        assert resp.status_code == 201
        data = resp.json()
        assert "id" in data
        assert isinstance(data["id"], str)

    def test_list_events(self, client):
        client.post("/api/events", json=self._create_event_payload("_list"))
        resp = client.get("/api/events")
        assert resp.status_code == 200
        data = resp.json()
        assert "total" in data
        assert "events" in data
        assert len(data["events"]) >= 1

    def test_get_event(self, client):
        create_resp = client.post("/api/events", json=self._create_event_payload("_get"))
        event_id = create_resp.json()["id"]

        resp = client.get(f"/api/events/{event_id}")
        assert resp.status_code == 200
        data = resp.json()
        assert data["id"] == event_id
        assert data["category"] == "politics"
        assert len(data["titles"]) == 2

    def test_get_event_not_found(self, client):
        resp = client.get("/api/events/nonexistent-id")
        assert resp.status_code == 404

    def test_update_event(self, client):
        create_resp = client.post("/api/events", json=self._create_event_payload("_upd"))
        event_id = create_resp.json()["id"]

        resp = client.put(f"/api/events/{event_id}", json={"importance": 95})
        assert resp.status_code == 200
        assert resp.json()["status"] == "updated"

        get_resp = client.get(f"/api/events/{event_id}")
        assert get_resp.json()["importance"] == 95

    def test_delete_event(self, client):
        create_resp = client.post("/api/events", json=self._create_event_payload("_del"))
        event_id = create_resp.json()["id"]

        resp = client.delete(f"/api/events/{event_id}")
        assert resp.status_code == 200

        get_resp = client.get(f"/api/events/{event_id}")
        assert get_resp.status_code == 404


class TestEventFilters:
    @pytest.fixture
    def seeded_events(self, client):
        events = [
            {"date": "1950-01-01", "date_precision": "year", "category": "military",
             "tags": ["war", "korean war"], "importance": 90,
             "titles": [{"language": "en", "title": "Korean War"}],
             "descriptions": [{"language": "en", "summary": "War summary"}]},
            {"date": "1978-12-01", "date_precision": "month", "category": "economy",
             "tags": ["reform", "deng xiaoping"], "importance": 100,
             "titles": [{"language": "en", "title": "Reform & Opening"}],
             "descriptions": [{"language": "en", "summary": "Deng's reform"}]},
            {"date": "2001-12-11", "date_precision": "day", "category": "economy",
             "tags": ["wto", "trade"], "importance": 85,
             "titles": [{"language": "en", "title": "WTO Accession"}],
             "descriptions": [{"language": "en", "summary": "China joins WTO"}]},
        ]
        ids = []
        for ev in events:
            resp = client.post("/api/events", json=ev)
            ids.append(resp.json()["id"])
        return ids

    def test_filter_by_category(self, client, seeded_events):
        resp = client.get("/api/events?category=economy")
        assert resp.status_code == 200
        data = resp.json()
        ids = [e["category"] for e in data["events"]]
        assert all(c == "economy" for c in ids)

    def test_filter_by_tags(self, client, seeded_events):
        resp = client.get("/api/events?tags=war")
        assert resp.status_code == 200
        data = resp.json()
        assert len(data["events"]) == 1
        assert "war" in data["events"][0]["tags"]

    def test_filter_by_multiple_tags(self, client, seeded_events):
        resp = client.get("/api/events?tags=reform,deng+xiaoping")
        assert resp.status_code == 200
        data = resp.json()
        assert len(data["events"]) == 1

    def test_filter_by_date_range(self, client, seeded_events):
        resp = client.get("/api/events?date_from=1970-01-01&date_to=1990-01-01")
        assert resp.status_code == 200
        data = resp.json()
        assert len(data["events"]) == 1
        assert data["events"][0]["category"] == "economy"

    def test_filter_by_importance(self, client, seeded_events):
        resp = client.get("/api/events?importance_min=90")
        assert resp.status_code == 200
        data = resp.json()
        assert all(e["importance"] >= 90 for e in data["events"])

    def test_search_by_query(self, client, seeded_events):
        resp = client.get("/api/events?q=War")
        assert resp.status_code == 200
        data = resp.json()
        assert len(data["events"]) >= 1

    def test_limit_and_offset(self, client, seeded_events):
        resp = client.get("/api/events?limit=1&offset=1")
        assert resp.status_code == 200
        data = resp.json()
        assert len(data["events"]) == 1




class TestMetadataEndpoints:
    def test_categories(self, client):
        client.post("/api/events", json={
            "date": "2020-01-01", "category": "society",
            "titles": [{"language": "en", "title": "Test"}],
        })
        resp = client.get("/api/events/categories")
        assert resp.status_code == 200
        assert "society" in resp.json()

    def test_languages(self, client):
        client.post("/api/events", json={
            "date": "2020-01-01",
            "titles": [{"language": "en", "title": "Lang Test"}],
        })
        resp = client.get("/api/events/languages")
        assert resp.status_code == 200
        assert "en" in resp.json()

    def test_tags(self, client):
        client.post("/api/events", json={
            "date": "2020-01-01", "tags": ["unique_test_tag_xyz"],
            "titles": [{"language": "en", "title": "Tag Test"}],
        })
        resp = client.get("/api/events/tags")
        assert resp.status_code == 200
        assert "unique_test_tag_xyz" in resp.json()

    def test_stats(self, client):
        resp = client.get("/api/events/stats")
        assert resp.status_code == 200
        data = resp.json()
        assert "total" in data
        assert "categories" in data
        assert "decades" in data


class TestGeoEndpoint:
    def test_geo_events(self, client):
        client.post("/api/events", json={
            "date": "2020-01-01", "category": "politics",
            "titles": [{"language": "en", "title": "Geo Test"}],
            "location": {"lat": 35.0, "lng": 135.0, "country": "JP", "names": {"en": "Tokyo"}},
        })
        resp = client.get("/api/events/geo")
        assert resp.status_code == 200
        data = resp.json()
        assert data["type"] == "FeatureCollection"
        assert len(data["features"]) >= 1
