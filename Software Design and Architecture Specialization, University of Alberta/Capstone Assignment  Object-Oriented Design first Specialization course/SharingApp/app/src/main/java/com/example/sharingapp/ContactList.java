package com.example.sharingapp;

import android.content.Context;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.lang.reflect.Type;
import java.util.ArrayList;

public class ContactList {
    private ArrayList<Contact> contacts;
    private  String FILENAME = "contact.sav";

    public  ContactList()
    {
        contacts = new ArrayList<Contact>();
    }

    public void setContacts(ArrayList<Contact> contacts) { this.contacts = contacts;}
    public ArrayList<Contact> getContacts(){return  contacts;}
    public ArrayList<String> getAllUsernames(){
        ArrayList<String> user_names = new ArrayList <String>();
        for(Contact con : contacts)
            user_names.add(con.getUsername());
        return user_names;

    }
    public void addContact(Contact contact){contacts.add(contact);}
    public void deleteContact(Contact contact){contacts.remove(contact);}
    public Contact getContact(int index){
        return  contacts.get(index);
    }
    public int getSize(){return  contacts.size();}
    public int getIndex(Contact contact){
        for (int i = 0 ; i <contacts.size();i++)
        {
            if(contacts.get(i).getUsername().equals(contact.getUsername()))
                return i;
        }
        return 0;
    }
    public boolean hasContact(Contact contact){return (contacts.contains(contact));}//make it 0
    public Contact getContactByUsername(String username){
        for(Contact con : contacts)
            if(con.getUsername().equals(username))
                return con;
        return null;
    }
    public boolean isUsernameAvailable(String username){
        for(Contact con : contacts)
            if(con.getUsername().equals(username))
                return false;
        return true;
    }
    public void loadContacts(Context context)
    {
        try {
            FileInputStream fis = context.openFileInput(FILENAME);
            InputStreamReader isr = new InputStreamReader(fis);
            Gson gson = new Gson();
            Type listType = new TypeToken<ArrayList<Contact>>(){}.getType();
            contacts = gson.fromJson(isr, listType); // temporary
            fis.close();
        }
        catch (FileNotFoundException e) {
            contacts = new ArrayList<Contact>();
        }
     catch (IOException e) {
            contacts = new ArrayList<Contact>();
        }
    }

    public void saveContacts(Context context){
        try {
            FileOutputStream fos = context.openFileOutput(FILENAME, 0);
            OutputStreamWriter osw = new OutputStreamWriter(fos);
            Gson gson = new Gson();
            gson.toJson(contacts, osw);
            osw.flush();
            fos.close();
        }
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }

}

