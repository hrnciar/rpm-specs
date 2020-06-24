# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename bluebird

Name:               nodejs-bluebird
Version:            3.5.4
Release:            3%{?dist}
Summary:            Full featured Promises/A+ implementation

License:            MIT
URL:                https://www.npmjs.org/package/bluebird
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch
%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      nodejs-packaging >= 6



%if 0%{?enable_tests}
BuildRequires:  npm(acorn)
BuildRequires:  npm(acorn-walk)
BuildRequires:  npm(baconjs)
BuildRequires:  npm(bluebird)
BuildRequires:  npm(body-parser)
BuildRequires:  npm(browserify)
BuildRequires:  npm(cli-table)
BuildRequires:  npm(co)
BuildRequires:  npm(cross-spawn)
BuildRequires:  npm(glob)
BuildRequires:  npm(grunt-saucelabs)
BuildRequires:  npm(highland)
BuildRequires:  npm(istanbul)
BuildRequires:  npm(jshint)
BuildRequires:  npm(jshint-stylish)
BuildRequires:  npm(kefir)
BuildRequires:  npm(mkdirp)
BuildRequires:  npm(mocha)
BuildRequires:  npm(open)
BuildRequires:  npm(optimist)
BuildRequires:  npm(rimraf)
BuildRequires:  npm(rx)
BuildRequires:  npm(serve-static)
BuildRequires:  npm(sinon)
BuildRequires:  npm(uglify-js)
%endif


%description
Bluebird is a fully featured promise library with focus on innovative features
and performance

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%build

%install
find package.json js/ -type f \
    -exec install -m0644 -D '{}' '%{buildroot}%{nodejs_sitelib}/bluebird/{}' \;

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
grunt test
%endif


%files
%doc LICENSE README.md
%dir %{nodejs_sitelib}/bluebird
%{nodejs_sitelib}/bluebird/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Jan Staněk <jstanek@redhat.com> - 3.5.4-1
- Upgrade to latest upstream release.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 20 2015 Ralph Bean <rbean@redhat.com> - 2.9.12-1
- new version

* Wed Dec 10 2014 Ralph Bean <rbean@redhat.com> - 2.3.11-1
- Latest upstream.

* Mon Aug 18 2014 Ralph Bean <rbean@redhat.com> - 2.3.0-1
- Latest upstream.

* Tue Jul 22 2014 Ralph Bean <rbean@redhat.com> - 2.2.2-1
- Initial packaging for Fedora.
