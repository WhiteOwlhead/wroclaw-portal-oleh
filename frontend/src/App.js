/* eslint-disable prettier/prettier */
import './css/App.css';
import 'bootstrap/dist/css/bootstrap.css';
import 'C:/7SEMESTER/wroclaw-portal/frontend/src/css/Currency.css';
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from 'react-router-dom';
import { Container } from 'react-bootstrap';
import axios from 'axios';
import Header from './components/Header';
import Footer from './components/Footer';
import HomeScreen from './screens/HomeScreen';
import UniversityScreen from './screens/UniversityScreen';
import CurrencyScreen from './screens/CurrencyScreen';
import DocumentsScreen from './screens/DocumentsScreen';
import ForumScreen from './screens/ForumScreen';
import MapScreen from './screens/MapScreen';
import NewsScreen from './screens/NewsScreen';
import QaScreen from './screens/QaScreen';
import LoginScreen from './screens/LoginScreen';
import HomeContentScreen from './screens/HomeContentScreen';
import { useState, useEffect } from 'react';
import { NewsContextProvider } from './NewsContext';
import News from './components/News';
import SignupScreen from './screens/SignupScreen';
import HomeTextComponent from './components/HomeTextComponent';
//import Univercity from './components/Univercity';

const API_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';



// news api for



const App = () => {
  const [uniSearchWord, setUniSearchWord] = useState('');
  const [unis, setUnis] = useState([]);

  const handleSearchUni = async (e) => {
    e.preventDefault();
    console.log(uniSearchWord);

    // fetch()
    //   .then((res) => res.json())
    //   .then((data) => {
    //     setUnis([data, ...unis]);
    //     console.log(unis);
    //   })
    //   .catch((err) => {
    //     console.error(err);
    //   });

    try {
      const res = await axios.get(`${API_URL}/unis`);
      console.log([res.data]);
      //setUnis([res.data, ...unis]);
      setUnis(res.data || []);
    } catch (error) {
      console.log(error);
    }

    setUniSearchWord('');
  };

  //console.log(uniSearchWord);

  return (
    <Router>
      
      <HomeScreen />
      <Header title="Wroclaw Portal" />
      
      
      <main>
        <Container>
          <Routes>
            <Route exact path="/currency" element={<CurrencyScreen />} />
            <Route
              exact
              path="/uni"
              element={
                <UniversityScreen
                  handleSubmit={handleSearchUni}
                  uniSearchWord={uniSearchWord}
                  setUniSearchWord={setUniSearchWord}
                  unis={unis}
                  setUnis={setUnis}
                />
              }
            />
            <Route exact path="/news" element={<NewsScreen />} />
            <Route exact path="/map" element={<MapScreen />} />
            <Route exact path="/forum" element={<ForumScreen />} />
            <Route exact path="/docs" element={<DocumentsScreen />} />
            <Route exact path="/qa" element={<QaScreen />} />
            <Route exact path="/login" element={<LoginScreen />} />
            <Route exact path="/signup" element={<SignupScreen />} />
            <Route exact path="/" element={<HomeContentScreen />} />
            
            
          </Routes>
        </Container>
      </main>

      <Footer />
    </Router>
  );
};

export default App;
