%global driver eqmod

Name:           indi-%{driver}
Version:        1.8.1
Release:        2%{?dist}
Summary:        INDI driver providing support for SkyWatcher Protocol

License:        GPLv3+
URL:            http://indilib.org/
# Upstream provides one big tar including nonfree BLOBs for other drivers.
# Thus we have to generate a clean tar by ourself containing only
# the free driver to be packaged using
# ./indi-eqmod-generate-tarball.sh 1.3.1
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-generate-tarball.sh

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:  gsl-devel
BuildRequires:	libnova-devel
BuildRequires:	zlib-devel
BuildRequires:  libindi = %{version}
BuildRequires:  libindi-devel = %{version}

# We have to specify this requirement as the shared libraries are part of
# libindi-libs (which is what the dependency generator will find), but the
# driver also requires the binary indiserver, part of libindi package.
Requires:     libindi = %{version}

%description
INDI driver adding support for telescope mounts using the 
SkyWatcher protocol.


%prep
%setup -q -n%{name}-%{version}


%build
%cmake
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc AUTHORS COPYING INSTALL README
%{_bindir}/indi_eqmod_telescope
%{_datadir}/indi/indi_*.xml


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 20 2019 Christian Dersch <lupinix@fedoraproject.org> - 1.8.1-1
- new version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Christian Dersch <lupinix@mailbox.org> - 1.7.7-1
- new version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.7.4-2
- Rebuild with fixed binutils

* Sun Jul 29 2018 Christian Dersch <lupinix@mailbox.org> - 1.7.4-1
- new version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 1.7.2-1
- new version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Christian Dersch <lupinix@mailbox.org> - 1.6.2-1
- new version

* Tue Jan 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 1.6.0-1
- new version

* Sat Oct 07 2017 Christian Dersch <lupinix@mailbox.org> - 1.5.0-1
- new version

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon Feb 27 2017 Christian Dersch <lupinix@mailbox.org> - 1.4.1-1
- new version

* Sun Feb 26 2017 Christian Dersch <lupinix@mailbox.org> - 1.4.0-1
- new version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Christian Dersch <lupinix@mailbox.org> - 1.3.1-1
- new version

* Tue Feb 02 2016 Christian Dersch <lupinix@fedoraproject.org> - 1.2.0-1.20160202svn2675
- updated to libindi 1.2.0 tree

* Mon Sep 07 2015 Christian Dersch <lupinix@fedoraproject.org> - 1.1.0-1.20150907svn2392
- updated to libindi 1.1.0 tree

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3.20150226svn2046
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-2.20150226svn2046
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 26 2015 Christian Dersch <lupinix@fedoraproject.org> - 1.0.0-1.20150226svn2046
- updated to libindi 1.0.0 tree

* Sat Oct 25 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.9.9-3.20141015svn1783
- fixed wrong macro usage

* Wed Oct 15 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.9.9-2.20141015svn1783
- small spec fix

* Wed Oct 15 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.9.9-1.20141015svn1783
- initial spec
