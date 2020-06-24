# The tests use bundled 'vendor/mt.js/node-mt.js' and unpackaged nodejs-buster.
%global enable_tests 0

%if 0%{?fedora} || 0%{?rhel} >= 7
%global installdir  %{_jsdir}/zlib
%else
%global installdir  %{_datadir}/javascript/zlib
%endif

Name:            js-zlib
Version:         0.2.0
Release:         15%{?dist}
Summary:         JavaScript library reimplementing compression

License:         MIT
URL:             https://github.com/imaya/zlib.js
Source0:         http://registry.npmjs.org/zlibjs/-/zlibjs-%{version}.tgz

BuildArch:       noarch

BuildRequires:   ant
BuildRequires:   closure-compiler
BuildRequires:   python3
BuildRequires:   jarjar
BuildRequires:   junit

%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:   web-assets-devel
Requires:        web-assets-filesystem
%endif

%if 0%{?enable_tests}
BuildRequires:   npm(buster)
%endif

%description
zlib.js is ZLIB(RFC1950), DEFLATE(RFC1951), GZIP(RFC1952), and
PKZIP implementation in JavaScript. This library can be used to
perform compression and decompression in the browser.


%prep
echo "Settings: enable_tests=%{?enable_tests}"

%setup -q -n package

# Remove bundled and pre-built files.
rm -rf bin/* vendor/

# arguments.callee is forbidden in strict mode
sed -i s/arguments.callee.caller/null/ closure-primitives/base.js

# Use system closure-compiler to build.
sed -i -e 's#<java jar="${compiler}" fork="true"#<exec executable="closure-compiler"#' \
       -e 's#</java>#</exec>#' \
       -e 's#PERFORMANCE_OPTIMIZATIONS#ADVANCED_OPTIMIZATIONS#' \
       -e 's#executable="python"#executable="python3"#' \
    build.xml


%build
/usr/bin/ant all


%install
mkdir -p %{buildroot}%{installdir}
cp -p bin/*.min.js bin/*.min.js.map bin/node-zlib.js \
    %{buildroot}%{installdir}


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/buster-test
%endif


%files
%license LICENSE
%doc ChangeLog.md README.md README.en.md
%{installdir}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Tom Hughes <tom@compton.nu> - 0.2.0-12
- Use python3 for build

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 17 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.0-5
- also include .map files

* Mon Mar 17 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.0-4
- As it turns out, matching {_arch} won't solve our problem as it indicates
  the architecture of the build host not the target architecture. Instead
  split nodejs-zlibjs into a separate package, as otherwise js-zlib would be
  restricted to {nodejs_arches}. bin/node-zlib.js will remain in the js-zlib
  package, while nodejs-zlibjs will depend on js-zlib and have a symlink.
- add logic for building on EPEL 6

* Sun Mar 16 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.0-3
- Simplify the arches condition
- Restore sed instead of a patch

* Fri Mar 14 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.0-2
- add missing BuildArch: noarch
- nodejs-zlibjs should only be built for {nodejs_arches} but js-zlib package
  does not have this limitation, so add logic for building nodejs-zlibjs only
  on {nodejs_arches} while allowing js-zlib to be built on all architectures

* Thu Mar 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.0-1
- update to upstream release 0.2.0
- rename to js-zlib and nodejs-zlibjs
- install to {_jsdir}
- maintain filenames and locations that upstream are using
- use patch instead of sed
- include additional documentation in nodejs-zlibjs package

* Tue Oct 29 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.7-1
- Initial package.
