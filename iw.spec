Summary:	nl80211 based CLI
Name:		iw
Version:	3.15
Release:	1
License:	BSD
Group:		Networking/Admin
Source0:	https://www.kernel.org/pub/software/network/iw/%{name}-%{version}.tar.xz
# Source0-md5:	3b77ad7ec44a865a3bb2ab6c1c463bba
URL:		http://wireless.kernel.org/en/users/Documentation/iw
BuildRequires:	libnl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nl80211 based CLI configuration utility for wireless devices.

%prep
%setup -q

%{__sed} -i 's|-O2 -g|%{rpmcflags}|g' Makefile

%build
%{__make} V=1 CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/iw
%{_mandir}/man8/iw.8*

