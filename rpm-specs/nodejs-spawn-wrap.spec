%{?nodejs_find_provides_and_requires}

%global packagename spawn-wrap

# tests disabled because the depend on a newer version of npm(tap)
%global enable_tests 0

Name:		nodejs-spawn-wrap
Version:	1.3.8
Release:	6%{?dist}
Summary:	Wrap all spawned Node.js child processes with environs and args

License:	ISC
URL:		https://github.com/isaacs/spawn-wrap.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	tests-%{version}.tar.bz2
Source10:	dl-tests.sh

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(os-homedir)
BuildRequires:	npm(mkdirp)
BuildRequires:	npm(rimraf)
BuildRequires:	npm(signal-exit)
BuildRequires:	npm(which)
%if 0%{?enable_tests}
BuildRequires:	npm(foreground-child)
BuildRequires:	npm(tap)
%endif

%description
Wrap all spawned Node.js child processes by adding environs and arguments ahead
of the main JavaScript file argument.


%prep
%setup -q -n package
# tests
%setup -q -T -D -a 1 -n package

%nodejs_fixdep signal-exit

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js lib/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
/usr/bin/tap test/*.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 24 2017 Jared Smith <jsmith@fedoraproject.org> - 1.3.8-1
- Update to upstream 1.3.8 release

* Mon May 08 2017 Jared Smith <jsmith@fedoraproject.org> - 1.3.5-1
- Update to upstream 1.3.5 release

* Wed Jul 13 2016 Jared Smith <jsmith@fedoraproject.org> - 1.2.4-1
- Update to upstream 1.2.4 release

* Mon Feb 15 2016 Jared Smith <jsmith@fedoraproject.org> - 1.1.1-1
- Update to upstream 1.1.1 release

* Fri Nov 06 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.1-2
- Fix tests to run correctly

* Tue Oct 27 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.1-1
- Initial packaging
