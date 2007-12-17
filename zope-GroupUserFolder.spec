%define Product GroupUserFolder
%define product groupuserfolder
%define name    zope-%{Product}
%define version 3.55.1
%define bad_version %(echo %{version} | sed -e 's/\\./-/g')
%define release %mkrel 1

%define zope_minver      2.5
%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    GRUF is a convenient tool to manage groups of users within Zope
License:    Zope Public License (ZPL)
Group:      System/Servers
URL:        http://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/%{version}/%{product}-%{bad_version}.tgz
Requires:   zope >= %{zope_minver}
BuildArch:  noarch

%description
GRUF is a convenient tool to manage groups of users within Zope.

It works as a frontend between a Zope application relying on a UserFolder 
and a set of two regular UserFolders : one will store the users and the 
other one will store the groups.

It has a whole bunch of cool features, especially :
It doesn't patch anything in Zope ;
It integrates smoothly without the need of any additional form (some are 
provided but it's only for convenience) ;
It doesn't store users by itself but delegates that job to another User 
Folder. So, it works with virtually ANY Zope UserFolder in there ! 
(especially standard acl_users but also LDAPUserFolder, SimpleUserFolder...)

It supports groups nesting (ie. groups can belong to other groups and 
'inherit' their roles It allows groups and users to be stored in a separated 
backend (eg. groups in ZODB and users in LDAP, ...);
It supports (since 2.0 version) multiple user sources, ie. you can have a 
bunch of users in LDAP plus some users in a standard User Folder, and they all 
will be integrated to GRUF;

It provides clean management screens (including user and groups editing 
interfaces) ; It provides security auditing tools ; It's compatible with 
regular Zope UserFolder API ;
Groups are seen as regular Zope users in applications that doesn't include 
groups support. Thus, you don't have to rewrite anything to gain benefit from 
GRUF's groups !

GRUF has been designed by the Ingeniweb team.

%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
