import Pagination from '@mui/material/Pagination';
import Stack from '@mui/material/Stack';
import ForestCard from './ForestCard';
import './App.css';

function App() {
  return (
    <div className="App">
      <Stack direction="row" spacing={2}>
        <ForestCard />
        <ForestCard />
        <ForestCard />
        <ForestCard />
        <ForestCard />
        <ForestCard />
      </Stack>
      <Pagination count={10} />
    </div>
  );
}

export default App;
