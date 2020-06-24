%{?nodejs_find_provides_and_requires}

%global packagename type-is
%global enable_tests 1

Name:		nodejs-type-is
Version:	1.6.15
Release:	6%{?dist}
Summary:	Infer the content-type of a request

License:	MIT
URL:		https://github.com/jshttp/type-is
Source0:	https://github.com/jshttp/type-is/archive/%{version}.tar.gz

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(media-typer)
BuildRequires:	npm(mime-types)
%endif

%description
Infer the content-type of a request.


%prep
%setup -q -n %{packagename}-%{version}


%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc README.md HISTORY.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Jared Smith <jsmith@fedoraproject.org> - 1.6.15-1
- Update to upstream 1.6.15

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 29 2016 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.6.12-1
- Update to 1.6.12 (#1303399)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Jared Smith <jsmith@fedoraproject.org> - 1.6.11-1
- Update to upstream 1.6.11 release

* Mon Dec 07 2015 Jared Smith <jsmith@fedoraproject.org> - 1.6.10-1
- Update to upstream 1.6.10 release

* Wed Oct  7 2015 Jared Smith <jsmith@fedoraproject.org> - 1.6.9-1
- Initial packaging
