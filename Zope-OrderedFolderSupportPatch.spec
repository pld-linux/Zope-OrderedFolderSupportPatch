%include	/usr/lib/rpm/macros.python
%define		zope_subname	OrderedFolderSupportPatch
Summary:	This is a patch-product that modifies ObjectManager
Summary(pl):	Poprawka modyfikuj±ca ObjectManagera
Name:		Zope-%{zope_subname}
Version:	1.0
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	OrderedFolderSupportPatch.tar.gz
URL:		http://www.nuxeo.org
BuildRequires:	python >= 2.2
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope >= 2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a patch-product that modifies ObjectManager to allow folders
to be ordered by the user.

%description -l pl
Poprawka modyfikuj±ca dostêp do ObjectManagera przez u¿ytkownika.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af *.py $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
        /usr/sbin/installzopeproduct -d %{zope_subname}
        if [ -f /var/lock/subsys/zope ]; then
                /etc/rc.d/init.d/zope restart >&2
        fi
fi

%files
%defattr(644,root,root,755)
%doc CHANGES HISTORY LICENSE.txt README.txt
%{_datadir}/%{name}
