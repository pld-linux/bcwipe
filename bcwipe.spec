Summary:	Securely erase data from magnetic and solid-state memory
Summary(pl):	Bezpieczne usuwanie danych z pamiêci magnetycznych
Name:		BCWipe
Version:	1.5
Release:	0.1
License:	See LICENSE
Group:		Applications/System
Source0:	http://www.jetico.com/linux/%{name}-%{version}-3.tar.gz
URL:		http://www.jetico.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Securely erase data from magnetic and solid-state memory.

%description -l pl
Bezpieczne usuwanie danych z pamiêci magnetycznych.

%prep
%setup -q -n bcwipe

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
	install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_prefix}/man/man1
install -d $RPM_BUILD_ROOT%{_mandir}/man1
	make install root=$RPM_BUILD_ROOT

%__os_install_post
# build directory and file lists
#find $RPM_BUILD_ROOT -type d | sed -e "s#^$RPM_BUILD_ROOT#%attr(-, root, root) %dir #g" > rpm-files

find $RPM_BUILD_ROOT -type f | sed -e "s#^$RPM_BUILD_ROOT#%attr(-, root, root) #g" > rpm-files
find $RPM_BUILD_ROOT -type l | sed -e "s#^$RPM_BUILD_ROOT#%attr(-, root, root) #g" >> rpm-files
find $RPM_BUILD_ROOT -type b | sed -e "s#^$RPM_BUILD_ROOT#%attr(-, root, root) #g" >> rpm-files

%clean
rm -rf $RPM_BUILD_ROOT

%files -f rpm-files
%defattr(644,root,root,755)

%doc LICENSE
