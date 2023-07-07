import { ChangeEvent, useState, useEffect } from 'react';
import { Modal, ModalOverlay, ModalContent, ModalHeader, ModalFooter, ModalBody, ModalCloseButton, Button, Heading, Box, Input } from '@chakra-ui/react';
import axios from 'axios';

const initialUpdateDishData = { id: '', name: '', stock: 0, price: 0 };

interface Props {
     onClose(): void;
     getData(): void;
     isOpen: boolean;
     data: typeof initialUpdateDishData;
}

const UpdateDishModal: React.FC<Props> = ({ onClose, isOpen, data, getData }) => {
     const [updateDishData, setUpdateDishData] = useState(initialUpdateDishData);



     const update_dish = () => {
          axios.post(`/update/${updateDishData.id}`, updateDishData)
               .then(() => {
                    getData()
                    setUpdateDishData(initialUpdateDishData);
                    onClose()
               })
               .catch((err) => console.log(err));
     };

     const handleChangeUpdate = (e: ChangeEvent<HTMLInputElement>) => {
          const { name, value, type } = e.target;
          setUpdateDishData((prev) => ({
               ...prev,
               [name]: type === 'number' ? parseFloat(value) : value
          }));
     };

     useEffect(() => {
          if (data && data.name) {
               setUpdateDishData(data);
          } else {
               setUpdateDishData(initialUpdateDishData);
          }
     }, [data]);

     return (
          <Modal isOpen={isOpen} onClose={onClose}>
               <ModalOverlay />
               <ModalContent>
                    <ModalHeader>Update Data</ModalHeader>
                    <ModalCloseButton />
                    <ModalBody>
                         <Box w="100%" p="1rem" display="grid" gap="1rem" >
                              <Input name="name" value={updateDishData.name} placeholder="Enter the Dish name" onChange={handleChangeUpdate} />
                              <Input type="number" value={updateDishData.price} name="price" placeholder="Enter the Dish price" onChange={handleChangeUpdate} />
                              <Input type="number" value={updateDishData.stock} name="stock" placeholder="Enter the Dish stock" onChange={handleChangeUpdate} />
                         </Box>
                    </ModalBody>
                    <ModalFooter>
                         <Button colorScheme="blue" mr={3} onClick={onClose}>
                              Close
                         </Button>
                         <Button variant="ghost" onClick={update_dish}>Update</Button>
                    </ModalFooter>
               </ModalContent>
          </Modal>
     );
};

export default UpdateDishModal;
