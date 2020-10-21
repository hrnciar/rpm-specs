%{?nodejs_find_provides_and_requires}

%global packagename mime-types
%global enable_tests 1

Name:		nodejs-mime-types
Version:	2.1.17
Release:	8%{?dist}
Summary:	The ultimate javascript content-type utility

License:	MIT
URL:		https://github.com/jshttp/mime-types
Source0:	https://github.com/jshttp/%{packagename}/archive/%{version}.tar.gz

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(mime-db)
%endif

Requires:	nodejs

%description
The ultimate javascript content-type utility

%prep
%setup -q -n %{packagename}-%{version}

%nodejs_fixdep mime-db '^1.19.0'

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/mocha -R spec
%endif


%files
%doc README.md HISTORY.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}



%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.17-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 06 2017 Jared Smith <jsmith@fedoraproject.org> - 2.1.17-1
- Update to upstream 2.1.17

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 16 2016 Jared Smith <jsmith@fedoraproject.org> - 2.1.10-1
- Update to upstream 2.1.10 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 09 2016 Jared Smith <jsmith@fedoraproject.org> - 2.1.9-1
- Update to upstream 2.1.9 release

* Thu Dec 03 2015 Jared Smith <jsmith@fedoraproject.org> - 2.1.8-1
- Update to upstream 2.1.8 release

* Thu Nov 19 2015 Jared Smith <jsmith@fedoraproject.org> - 2.1.7-2
- Relax requirement on version of npm(mime-db)

* Wed Oct  7 2015 Jared Smith <jsmith@fedoraproject.org> - 2.1.7-1
- Initial packaging
