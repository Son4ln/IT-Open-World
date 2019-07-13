<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Post extends Model
{
    protected $table = "posts_post";

    protected $fillable = ['avatar', 'title', 'slug', 'content', 'origin', 'status', 'creator_id', 'last_modified_by_id', 'user_id'];

    protected $casts = [
    	'created_at' => 'datetime',
    	'updated_at' => 'datetime',
    	// 'deleted_at' => 'datetime',
    ];

    public function users()
    {
    	return $this->belongsTo('App\User');
    }

    public function series()
    {
    	return $this->belongsToMany('App\Series');
    }

    public function files()
    {
    	return $this->belongsToMany('App\FilePost');
    }

    public function reports()
    {
    	return $this->belongsToMany('App\PostReport');
    }

    public function saves()
    {
    	return $this->belongsToMany('App\PostSave');
    } 
}
