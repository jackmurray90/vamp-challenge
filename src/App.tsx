import React, {useState, useEffect} from 'react';
import './App.css';
import config from './config';

interface Campaign {
  name: string;
  startDate: string;
  endDate: string;
  budget: number;
  hashtags: string;
  teamName: string;
  description: string;
}

function App() {
  const [campaigns, setCampaigns] = useState<Campaign[]>([]);

  useEffect(() => {
    fetch(config.API_HOST + "/list_campaigns")
      .then(response => response.json())
      .then(response => setCampaigns(response));
  }, []);

  return (
    <div className="App">
      <h1>List of campaigns</h1>
      {campaigns.length === 0 && "Loading..."}
      {campaigns.length > 0 &&
        <table>
          <tr>
            <th>Name</th>
            <th>Start Date</th>
            <th>End Date</th>
            <th>Budget</th>
            <th>Hashtags</th>
            <th>Team Name</th>
            <th>Description</th>
          </tr>
          {campaigns.map((campaign) =>
            <tr>
              <td>{campaign.name}</td>
              <td>{campaign.startDate}</td>
              <td>{campaign.endDate}</td>
              <td>{campaign.budget}</td>
              <td>{campaign.hashtags}</td>
              <td>{campaign.teamName}</td>
              <td>{campaign.description}</td>
            </tr>
          )}
        </table>
      }
    </div>
  );
}

export default App;
