%{?nodejs_find_provides_and_requires}

%global packagename tap-mocha-reporter
%global enable_tests 1

Name:		nodejs-tap-mocha-reporter
Version:	0.0.24
Release:	9%{?dist}
Summary:	Format a TAP stream using Mocha's set of reporters

License:	ISC and MIT
URL:		https://github.com/isaacs/tap-mocha-reporter.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

# The test depends on a *really* old version of tap, and can easily be
# re-written to use the new tap syntax
Patch0:		tap-mocha-reporter_fix-test.patch

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	npm(debug)
BuildRequires:	npm(diff)
BuildRequires:	npm(escape-string-regexp)
BuildRequires:	npm(glob)
BuildRequires:	npm(js-yaml)
BuildRequires:	npm(supports-color)
BuildRequires:	npm(tap)
BuildRequires:	npm(tap-parser)
BuildRequires:	npm(unicode-length)

%endif

%description
Format a TAP stream using Mocha's set of reporters


%prep
%setup -q -n package
%patch0 -p2

chmod -x index.js

%nodejs_fixdep diff
%nodejs_fixdep supports-color



%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js lib/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/tap test/*.js
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Jared Smith <jsmith@fedoraproject.org> - 0.0.24-1
- Update to upstream 0.0.24 release

* Mon Jan 18 2016 Jared Smith <jsmith@fedoraproject.org> - 0.0.22-3
- Add MIT license to license tag

* Mon Jan 18 2016 Jared Smith <jsmith@fedoraproject.org> - 0.0.22-2
- Fix build dependencies

* Mon Jan 18 2016 Jared Smith <jsmith@fedoraproject.org> - 0.0.22-1
- Update to upstream 0.0.22 release

* Sat Oct 31 2015 Jared Smith <jsmith@fedoraproject.org> - 0.0.21-2
- Relax dependency version of several newer npm modules

* Tue Oct 27 2015 Jared Smith <jsmith@fedoraproject.org> - 0.0.21-1
- Initial packaging
