Summary:	Securely erase data from magnetic and solid-state memory
Summary(pl.UTF-8):	Bezpieczne usuwanie danych z pamięci magnetycznych
Name:		bcwipe
Version:	1.9
Release:	1
License:	commercial with 30-day trial period (see COPYING)
Group:		Applications/System
Source0:	http://www.jetico.com/linux/BCWipe-%{version}-3.tar.gz
# Source0-md5:	500dc22f5a2a2e3b52ec597bc7d17452
URL:		http://www.jetico.com/
BuildRequires:	autoconf
BuildRequires:	automake
Obsoletes:	BCWipe
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Securely erase data from magnetic and solid-state memory.

%description -l pl.UTF-8
Bezpieczne usuwanie danych z pamięci magnetycznych.

%prep
%setup -q -n %{name}-%{version}-3

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/bcwipe
%{_mandir}/man1/bcwipe.1*
