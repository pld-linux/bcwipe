Summary:	Securely erase data from magnetic and solid-state memory
Summary(pl):	Bezpieczne usuwanie danych z pamiêci magnetycznych
Name:		bcwipe
Version:	1.5
Release:	0.1
License:	See LICENSE
Group:		Applications/System
Source0:	http://www.jetico.com/linux/BCWipe-%{version}-3.tar.gz
# Source0-md5:	1b99a6d12c2b3259fdbd527f484f03c3
URL:		http://www.jetico.com/
Obsoletes:	BCWipe
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Securely erase data from magnetic and solid-state memory.

%description -l pl
Bezpieczne usuwanie danych z pamiêci magnetycznych.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
