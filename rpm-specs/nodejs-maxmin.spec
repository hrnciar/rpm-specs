%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:           nodejs-maxmin
Version:        2.1.0
Release:        9%{?dist}
Summary:        Get pretty output of the original, minified gzipped size of a string/buffer

License:        MIT
URL:            https://github.com/sindresorhus/maxmin
Source0:        https://github.com/sindresorhus/maxmin/archive/v%{version}/maxmin-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(chalk)
BuildRequires:  npm(figures)
BuildRequires:  npm(gzip-size)
BuildRequires:  npm(pretty-bytes)

%if 0%{?enable_tests}
BuildRequires:  npm(ava)
%endif

%description
%{summary}.


%prep
%autosetup -n maxmin-%{version}
%nodejs_fixdep chalk ^1.1.1
%nodejs_fixdep pretty-bytes

%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/maxmin
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/maxmin

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs -e "require('./')"
%if 0%{?enable_tests}
${binddir}/ava
%endif


%files
%doc readme.md screenshot.png
%license license
%{nodejs_sitelib}/maxmin


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Jared Smith <jsmith@fedoraproject.org> - 2.1.0-4
- Relax dependency on npm(pretty-bytes)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 28 2016 Tom Hughes <tom@compton.nu> - 2.1.0-1
- Update to 2.1.0 upstream release

* Mon Feb 22 2016 Tom Hughes <tom@compton.nu> - 0.2.0-5
- Update npm(chalk) dependency

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.0-1
- update to upstream release 0.2.0
- disable use of gzip-size on branches where js-zlib cannot be packaged

* Thu Mar 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.0-1
- initial package
