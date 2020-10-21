%global projname z

%global desc \
Tracks your most used directories, based on 'frecency'.\
\
After a short learning phase, z will take you to the most 'frecent'\
directory that matches ALL of the regexps given on the command line, in\
order.

Name:		%{projname}
Version:	1.11
Release:	2%{?dist}
Summary:	Maintains a jump-list of the directories you actually use
License:	WTFPL
Source0:	https://github.com/rupa/%{projname}/archive/v%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	gzip

%description %{desc}


%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_libexecdir}
install -pm 644 z.sh %{buildroot}%{_libexecdir}/z.sh
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 644 z.1 %{buildroot}%{_mandir}/man1/z.1

%check

%files
%{_libexecdir}/z.sh
%{_mandir}/man1/z.1*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Ben Cotton <bcotton@fedoraproject.org> - 1.11-0
- Update to latest upstream release

* Fri Oct 18 2019 Ben Cotton <bcotton@fedoraproject.org> - 1.9-0
- Initial packaging
