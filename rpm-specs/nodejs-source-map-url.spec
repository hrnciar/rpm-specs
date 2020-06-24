%{?nodejs_find_provides_and_requires}

%global packagename source-map-url
%global enable_tests 1
# tests temporarily disabled to bootstrap other packages

Name:		nodejs-source-map-url
Version:	0.4.0
Release:	6%{?dist}
Summary:	Tools for working with sourceMappingURL comments

License:	MIT
URL:		https://github.com/lydell/source-map-url
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(expect.js)
%endif

Requires:	nodejs

%description
Tools for working with sourceMappingURL comments.


%prep
%setup -q -n package

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr *.json *.json5 *.js \
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
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Apr 14 2017 Jared Smith <jsmith@fedoraproject.org> - 0.4.0-1
- Update to upstream 0.4.0 release

* Sun Oct 25 2015 Jared Smith <jsmith@fedoraproject.org> - 0.3.0-4
- Temporarily disable tests for bootstrapping

* Sat Oct 24 2015 Jared Smith <jsmith@fedoraproject.org> - 0.3.0-3
- Update build requirements

* Fri Oct 23 2015 Jared Smith <jsmith@fedoraproject.org> - 0.3.0-1
- Initial packaging
