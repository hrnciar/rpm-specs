%{?nodejs_find_provides_and_requires}

%global packagename testdata-w3c-json-form
%global enable_tests 1

Name:		nodejs-testdata-w3c-json-form
Version:	0.2.1
Release:	6%{?dist}
Summary:	Test data intended to be used by people building query parsers

License:	MIT
URL:		http://github.com/LinusU/testdata-w3c-json-form.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# license requested upstream at https://github.com/LinusU/testdata-w3c-json-form/issues/1
Source1:	LICENSE-MIT.txt

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
#BuildRequires:	
%endif

%description
This repository contains test data intended to be used by people building query
parsers that follows [the W3C JSON form
spec](http://www.w3.org/TR/html-json-forms/).


%prep
%autosetup -n package
cp -p %{SOURCE1} LICENSE

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

%files
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Jared Smith <jsmith@fedoraproject.org> - 0.2.1-1
- Update to upstream 0.2.1 release, with an MIT license

* Tue Oct  3 2017 Jared Smith <jsmith@fedoraproject.org> - 0.2.0-1
- Initial packaging
