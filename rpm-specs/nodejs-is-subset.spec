%{?nodejs_find_provides_and_requires}

%global packagename is-subset

# tests missing due to missing npm(babel)
%global enable_tests 0

Name:		nodejs-is-subset
Version:	0.1.1
Release:	8%{?dist}
Summary:	Check if an object is contained within another one

License:	MIT
URL:		https://github.com/studio-b12/is-subset
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	npm(babel)
BuildRequires:	npm(tap-spec)
%endif

%description
Check if an object is contained within another one


%prep
%autosetup -n package

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js module.js module/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/babel-node test.js | tap-spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc Readme.md
%license License.md
%{nodejs_sitelib}/%{packagename}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat May  6 2017 Jared Smith <jsmith@fedoraproject.org> - 0.1.1-1
- Initial packaging
