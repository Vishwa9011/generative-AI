import { Box, Button, Heading, Input, useDisclosure } from '@chakra-ui/react'
import axios from 'axios';
import { ChangeEvent, FormEvent, useCallback, useEffect, useState } from 'react'
import ListOrders from '../components/ListOrders/ListOrders';
import { dish } from '../constants/constants';
import UpdateDishModal from '../components/Models/UpdateDishModal';
import AddDishModals from '../components/Models/AddDishModals';


const Dishes = () => {
     const [dishes, setDishes] = useState([])
     const { isOpen, onOpen, onClose } = useDisclosure()
     const [updateDishData, setUpdateDishData] = useState<any>({});

     const { isOpen: isUpdateOpen, onOpen: OnUpdateOpen, onClose: onUpdateClose } = useDisclosure()

     const editData = useCallback((dish: dish) => {
          console.log('dish: ', dish);
          setUpdateDishData(dish);
          OnUpdateOpen();
     }, [])


     const getData = useCallback(() => {
          axios.get('dishes')
               .then(res => setDishes(res.data))
               .catch(err => console.log(err))
     }, [])

     useEffect(() => {
          getData()
     }, [])

     return (
          <Box>
               {isUpdateOpen && <UpdateDishModal isOpen={isUpdateOpen} onClose={onUpdateClose} getData={getData} data={updateDishData} />}
               {isOpen && <AddDishModals isOpen={isOpen} onClose={onClose} getData={getData} />}
               <Box p='1rem' display={'flex'} justifyContent={'flex-end'}>
                    <Button onClick={onOpen}>Add new Dish</Button>
               </Box>
               <hr />
               <Box>
                    {dishes && dishes.length > 0 && <ListOrders dishes={dishes} editData={editData} />}
               </Box>
          </Box>
     )
}

export default Dishes;


