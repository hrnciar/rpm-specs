Name:		nsdiff
Version:	1.77
Release:	3%{?dist}
Summary:	create an "nsupdate" script from DNS zone file differences

License:	Public Domain
URL:		https://dotat.at/prog/nsdiff/
# Alternative:
#Source0:	https://github.com/fanf2/%%{name}/archive/%%{name}-%%{version}.tar.gz
Source0:	https://dotat.at/prog/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	perl >= 5.10
BuildRequires:	perl(Pod::Man) perl(Pod::Html)
BuildRequires:	make
BuildArch:	noarch
Requires:	perl >= 5.10
Requires:	bind-utils bind-dnssec-utils

%description
The nsdiff program examines the old and new versions of a DNS zone, and
outputs the differences as a script for use by BIND's nsupdate program.
It provides a bridge between static zone files and dynamic updates.

The nspatch script is a wrapper around `nsdiff | nsupdate` that checks
and reports errors in a manner suitable for running from cron.

The nsvi script makes it easy to edit a dynamic zone.

%prep
%autosetup -n %{name}-%{version}

%build
make prefix=%{_prefix}


%install
%make_install prefix=%{_prefix}


%files
%doc README*
%{_bindir}/ns*
%{_mandir}/man1/ns*.1*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.77-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Petr Menšík <pemensik@redhat.com> - 1.77-1
- Initial version


