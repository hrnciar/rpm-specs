%{?nodejs_find_provides_and_requires}

%global packagename bundle-dependencies
%global enable_tests 1

Name:		nodejs-bundle-dependencies
Version:	1.0.2
Release:	11%{?dist}
Summary:	Generates bundledDependencies package.json value

License:	BSD
URL:		https://github.com/gajus/bundle-dependencies
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
Patch0:		nodejs-bundle-dependencies_fix-package-json.patch

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging

%description
Generates bundledDependencies package.json value using values of the
dependencies property.


%prep
%setup -q -n package
rm -rf node_modules
%patch0 -p1

%nodejs_fixdep yargs


# fix she-bang line and make executable
sed -i '1!b;s/env node/node/' dist/bin/index.js
chmod +x dist/bin/index.js

%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json dist/ %{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%if 0%{?enable_tests}
%{_bindir}/echo -e "\e[103m -=#=- There are no tests -=#=- \e[0m"
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 09 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.2-3
- Fix script interpreter in dist/bin/index.js

* Sun Jul 31 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.2-2
- Relax dependency on npm(yargs)

* Sat Jul 30 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.2-1
- Initial packaging
