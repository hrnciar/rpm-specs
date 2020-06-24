%{?nodejs_find_provides_and_requires}

# npm(chai) not yet available on EL6.
%if 0%{?fedora}
%global enable_tests 1
%else
%global enable_tests 0
%endif

Name:       nodejs-ain2
Version:    1.3.2
Release:    11%{?dist}
Summary:    A Node.js module for syslog logging (and a continuation of ain)
License:    MIT
URL:        https://github.com/phuesler/ain
Source0:    http://registry.npmjs.org/ain2/-/ain2-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(chai)
BuildRequires:  npm(mocha)
%endif

%description
This module provides syslog logging for Node.js.

Ain2 is written with full compatibility with the Node.js console module.
It implements all console functions and formatting. Ain2 also supports UTF-8.

Ain2 can send messages by UDP to 127.0.0.1:514 or to the a Unix socket such
as /dev/log.


%prep
%setup -q -n package
for i in CHANGELOG.md LICENSE readme.md; do
    sed 's/\r//' "${i}" > "${i}.new"
    touch -r "${i}" "${i}.new"
    mv "${i}.new" "${i}"
done


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/ain2
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/ain2

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
# Optional dependency npm(unix-dgram) not yet packaged for Fedora, so disable
# the test.
rm -f test/unix.spec.js
/usr/bin/mocha test/**/*.spec.js
%endif


%files
%doc CHANGELOG.md LICENSE readme.md
%{nodejs_sitelib}/ain2


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.3.2-1
- update to upstream release 1.3.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.1-6
- fix compatible arches on f18/el6

* Fri Jul 05 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.1-5
- restrict to compatible arches

* Fri May 31 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.1-4
- preserve timestamps when fixing new-line encoding

* Fri May 31 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.1-3
- disable tests as koji doesn't seem to like them (though they all pass
  in a local mock build)

* Sun May 26 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.1-2
- fix wrong file end of line encoding

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.1-1
- initial package
