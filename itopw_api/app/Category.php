<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Category extends Model
{
    protected $table = "categories_category";

    protected $fillable = ['avatar', 'name', 'slug', 'creator_id', 'last_modified_by_id'];

    protected $casts = [
    	'created_at' => 'datetime',
    	'updated_at' => 'datetime',
    	// 'deleted_at' => 'datetime',
    ];

    public function posts()
    {
    	return $this->belongsToMany('App\Post');
    }

    public function users()
    {
    	return $this->belongsTo('App\User');
    }
}
