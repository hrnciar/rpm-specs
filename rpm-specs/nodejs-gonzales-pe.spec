# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global prerelease 9
%global barename gonzales-pe

Name:               nodejs-gonzales-pe
Version:            3.0.0
Release:            0.11.%{prerelease}%{?dist}
Summary:            Gonzales Preprocessor Edition (fast CSS parser)

License:            MIT
URL:                https://www.npmjs.org/package/gonzales-pe
Source0:            http://registry.npmjs.org/gonzales-pe/-/gonzales-pe-3.0.0-%{prerelease}.tgz
BuildArch:          noarch

%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      nodejs-packaging >= 6

%if 0%{?enable_tests}
BuildRequires:      npm(coffee-script)
BuildRequires:      npm(benchmark)
BuildRequires:      npm(microtime)
BuildRequires:      npm(mocha)
%endif


%description
Gonzales is a fast CSS parser.
Gonzales PE is a rework with support of preprocessors.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/gonzales-pe
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/gonzales-pe

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
(mkdir -p log && node ./test/mocha.js) | tee ./log/test.log
%endif


%files
%doc CHANGELOG.md README.md MIT-LICENSE.txt doc/
%{nodejs_sitelib}/gonzales-pe/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.11.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.10.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.9.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.8.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.7.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.6.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.5.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.4.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-0.3.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jul 21 2014 Ralph Bean <rbean@redhat.com> - 3.0.0-0.2.9
- Specified noarch as per review.

* Wed Jul 16 2014 Ralph Bean <rbean@redhat.com> - 3.0.0-0.1.9
- Latest upstream.
- Fixed nodejs_fixdep statements.

* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 3.0.0-0.1.6
- Initial packaging for Fedora.
