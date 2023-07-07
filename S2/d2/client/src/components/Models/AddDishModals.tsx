import { ChangeEvent, FormEvent, useState } from 'react'
import { Modal, ModalOverlay, ModalContent, ModalHeader, ModalFooter, ModalBody, ModalCloseButton, Button, Box, Input } from '@chakra-ui/react'
import { v4 as uuid } from 'uuid';
import axios from 'axios';

const initialAddDishData = { name: "", stock: 0, price: 0 };

interface props {
     onClose(): void,
     getData(): void,
     isOpen: boolean
}

const AddDishModals = ({ onClose, isOpen, getData }: props) => {

     const [AddDishData, setAddDishData] = useState(initialAddDishData);

     const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
          if (e.target.type == 'number') {
               setAddDishData(prev => ({
                    ...prev, [e.target.name]: e.target.valueAsNumber
               }))
          } else {
               setAddDishData(prev => ({
                    ...prev, [e.target.name]: e.target.value
               }))
          }
     }

     const add_dish = (event: FormEvent) => {
          event.preventDefault();
          axios.post('/create', { id: uuid(), ...AddDishData })
               .then(() => {
                    getData()
                    setAddDishData(initialAddDishData)
                    onClose()
               })
               .catch(err => console.log(err))
     }

     return (
          <Modal isOpen={isOpen} onClose={onClose}>
               <ModalOverlay />
               <ModalContent>
                    <ModalHeader>Add Data</ModalHeader>
                    <ModalCloseButton />
                    <ModalBody>
                         <Box onSubmit={add_dish} as='form' w='100%' p='1rem' display={'grid'} gap='1rem'>
                              <Input name='name' value={AddDishData?.name || ''} placeholder='Enter the Dish name' onChange={handleChange} />
                              <Input type='number' value={AddDishData?.price || ''} name='price' placeholder='Enter the Dish price' onChange={handleChange} />
                              <Input type='number' value={AddDishData?.stock || ''} name='stock' placeholder='Enter the Dish stock' onChange={handleChange} />
                         </Box>
                    </ModalBody>
                    <ModalFooter>
                         <Button colorScheme='blue' mr={3} onClick={onClose}>
                              Close
                         </Button>
                         <Button variant='ghost' onClick={add_dish}>Add Dish</Button>
                    </ModalFooter>
               </ModalContent>
          </Modal>
     )
}

export default AddDishModals