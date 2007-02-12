Summary:	Securely erase data from magnetic and solid-state memory
Summary(pl.UTF-8):	Bezpieczne usuwanie danych z pamięci magnetycznych
Name:		bcwipe
Version:	1.6
Release:	1
License:	commercial with 30-day trial period (see LICENSE)
Group:		Applications/System
Source0:	http://www.jetico.com/linux/BCWipe-%{version}-3.tar.gz
# Source0-md5:	15064ad55c02631e802e92715cb940bb
URL:		http://www.jetico.com/
BuildRequires:	sed >= 4.0
Obsoletes:	BCWipe
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Securely erase data from magnetic and solid-state memory.

%description -l pl.UTF-8
Bezpieczne usuwanie danych z pamięci magnetycznych.

%prep
%setup -q -n %{name}

sed -i -e 's/-O /%{rpmcflags} /' Makefile

%build
%{__make} \
	CC="%{__cc}"

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
%attr(755,root,root) %{_bindir}/bcwipe
%{_mandir}/man1/bcwipe.1*
