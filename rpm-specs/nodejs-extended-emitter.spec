%{?nodejs_find_provides_and_requires}

%global packagename extended-emitter
%global enable_tests 1

Name:		nodejs-extended-emitter
Version:	1.0.2
Release:	7%{?dist}
Summary:	An emitter with expanded utility, UMD with dependencies for node and the browser

License:	MIT
URL:		https://github.com/khrome/extended-emitter.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz


BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(sift)
BuildRequires:	npm(wolfy87-eventemitter)

%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(should)
BuildRequires:	npm(vow)
%endif

%description
An emitter with expanded utility, UMD with dependencies for node and the browser


%prep
%autosetup -n package


%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json %{packagename}.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
NODE_ENV=test %{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Jared K. Smith <jsmith@fedoraproject.org> - 1.0.2-1
- Initial packaging
