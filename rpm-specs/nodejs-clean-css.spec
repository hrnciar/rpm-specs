# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

# jshint not in Fedora
%global enable_tests 0

%global barename clean-css

Name:               nodejs-%{barename}
Version:            4.2.1
Release:            3%{?dist}
Summary:            A well-tested CSS minifier

License:            MIT
URL:                https://www.npmjs.org/package/clean-css
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch

%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(source-map)
%if 0%{?enable_tests}
BuildRequires:      npm(browserify)
BuildRequires:      npm(http-proxy)
BuildRequires:      npm(nock)
BuildRequires:      npm(jshint)
BuildRequires:      npm(server-destroy)
BuildRequires:      npm(uglify-js)
BuildRequires:      npm(vows)
%endif

%description
Clean-css is a fast and efficient [Node.js](http://nodejs.org/) library for
minifying CSS files.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep source-map

%build

%install
find lib/ package.json index.js -type f \
    -exec install -D -m0644 '{}' '%{buildroot}%{nodejs_sitelib}/%{barename}/{}' \;

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
# vows  # test are not shipped via registry
%endif

%files
%doc README.md History.md
%license LICENSE
%dir %{nodejs_sitelib}/%{barename}
%{nodejs_sitelib}/%{barename}/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Jan Staněk <jstanek@redhat.com> - 4.2.1-1
- Upgrade to version 4.2.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 10 2016 Tom Hughes <tom@compton.nu> - 3.4.6-3
- Update npm(source-map) dependency

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Piotr Popieluch <piotr1212@gmail.com> - 3.4.6-1
- new version

* Thu Aug 27 2015 Piotr Popieluch <piotr1212@gmail.com> - 3.4.1-1
- new version

* Sat Jun 20 2015 Piotr Popieluch <piotr1212@gmail.com> - 3.3.3-1
- new version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Ralph Bean <rbean@redhat.com> - 3.1.8-1
- new version

* Sat Mar 14 2015 Piotr Popieluch <piotr1212@gmail.com> - 3.1.6-1
- Update to upstream 3.1.6
- Fixdep nodejs-source-map

* Wed Mar 04 2015 Ralph Bean <rbean@redhat.com> - 3.1.4-1
- new version

* Sun Feb 15 2015 Piotr Popieluch <piotr1212@gmail.com> - 3.0.3-1
- Update to upstream 3.0.3

* Wed Dec 24 2014 Parag Nemade <pnemade AT redhat.com> - 2.2.8-2
- Add missing cleancss binary

* Mon Jul 21 2014 Ralph Bean <rbean@redhat.com> - 2.2.8-1
- Latest upstream.
- Specify noarch.

* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 2.2.6-1
- Initial packaging for Fedora.
