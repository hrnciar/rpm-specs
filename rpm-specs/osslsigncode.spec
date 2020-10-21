%bcond_without tests

Name:       osslsigncode
Version:    2.1
Release:    1%{?dist}
Summary:    OpenSSL based Authenticode signing for PE/MSI/Java CAB files

License:    GPLv3+
URL:        https://github.com/mtrojnar/osslsigncode
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# To prevent network access during tests
Patch0:     %{name}-preventnetwork-access-during-tests.patch

# fix(tests): swallows the exit code
Patch1:     https://github.com/mtrojnar/osslsigncode/pull/61.patch#/%{name}-swallows-the-exit-code.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: coreutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: sed
BuildRequires: pkgconfig(libcrypto) >= 1.1.0
BuildRequires: pkgconfig(libcurl) >= 7.12.0
BuildRequires: pkgconfig(libgsf-1)
BuildRequires: pkgconfig(openssl) >= 1.1.0

%if %{with tests}
BuildRequires: gcab
BuildRequires: java-1.8.0-openjdk-headless
BuildRequires: libfaketime
BuildRequires: mingw64-gcc
BuildRequires: msitools
BuildRequires: openssl >= 1.1.0
BuildRequires: vim-common
%endif

%description
osslsigncode is a small tool that implements part of the functionality of the
Microsoft tool signtool.exe - more exactly the Authenticode signing and
timestamping. But osslsigncode is based on OpenSSL and cURL, and thus should
be able to compile on most platforms where these exist.


%prep
%autosetup -p1


%build
autoreconf -ifv
%configure \
    --with-curl \
    --with-gsf
%make_build


%install
%make_install


%check
# https://bugzilla.redhat.com/show_bug.cgi?id=1882547#c2
%if %{with tests}
pushd tests
echo 'int main(void) {return 0;}' | x86_64-w64-mingw32-gcc -x c -o putty.exe -
./testall.sh
popd
%endif


%files
%license LICENSE.txt COPYING.txt
%doc README.md README.unauthblob.md CHANGELOG.md TODO.md
%{_bindir}/%{name}


%changelog
* Wed Oct 14 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1-1
- build(update): 2.1
- build(test): add BR - gcab, libfaketime, msitools, vim-common for new v2.1

* Mon Oct 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0-4
- build: improvements per review rh#1882547
- test: improve tests and drop pre-built .exe binary

* Sun Oct 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0-3
- build: minor improvements per review rh#1882547
- test: add tests v1

* Fri Sep 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0-2
- style: spec

* Sun May 26 2019 gasinvein <gasinvein@gmail.com>
- Update to 2.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 30 2015 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.7.1-1
- New upstream release 1.7.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 14 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.5.2-1
- New upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 13 2011 Matthias Saou <matthias@saou.eu> 1.4-1
- Update to 1.4.
- Switch to make install DESTDIR since it works at last.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec  8 2009 Matthias Saou <matthias@saou.eu> 1.3.1-1
- Update to 1.3.1.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.3-3
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Matthias Saou <matthias@saou.eu> 1.3-1
- Update to 1.3.
- Remove now included hashfix patch.

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 1.2-5
- rebuild with new openssl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2-4
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.2-3
- Rebuild for deps

* Mon Aug 27 2007 Matthias Saou <matthias@saou.eu> 1.2-2
- Update License field.

* Tue Jan 30 2007 Matthias Saou <matthias@saou.eu> 1.2-1
- Initial RPM release.
