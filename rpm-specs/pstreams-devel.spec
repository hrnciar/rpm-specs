Name:           pstreams-devel
Version:        1.0.3
Release:        2%{?dist}
Summary:        POSIX Process Control in C++

License:        Boost
URL:            http://pstreams.sourceforge.net/
Source0:        http://downloads.sourceforge.net/pstreams/pstreams-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  perl
BuildRequires:  gawk
BuildArch:      noarch

%description
PStreams classes are like C++ wrappers for the POSIX.2 functions
popen(3) and pclose(3), using C++ iostreams instead of C's stdio
library.

%prep
%setup -q -n pstreams-%{version}

%build
make %{?_smp_mflags}
make docs

%install
make install  DESTDIR=$RPM_BUILD_ROOT includedir=%{_includedir}

%files
%license LICENSE_1_0.txt
%doc doc/html README AUTHORS ChangeLog
%{_includedir}/pstreams


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Jonathan Wakely <jwakely@redhat.com> - 1.0.3-1
- Update to version 1.0.3, change license info
- Add BuildRequires: for gcc-c++ and fix BuildRequires: for awk

* Mon Mar 09 2020 Jonathan Wakely <jwakely@redhat.com> - 0.8.1-13
- Add BuildRequires: for perl and awk

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Jonathan Wakely <jwakely@redhat.com> - 0.8.1-8
- Remove unnecessary Group tag and buildroot cleanup

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Jonathan Wakely <jwakely@redhat.com> - 0.8.1-3
- Sync spec file with upstream.

* Tue Jan 05 2016 Jonathan Wakely <jwakely@redhat.com> - 0.8.1-3
- Replace packagename macro and remove BuildRoot tag.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 0.8.1-1
- Update to 0.8.1 (bz#1111872)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May 12 2010 Jonathan Wakely <pstreams@kayari.org> - 0.7.0-1
- Add spec file to upstream repo and update.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 07 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.6.0-6
- timestamp patch (Till Mass)

* Fri Nov 07 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.6.0-5
- saving timestamp using "install -p"

* Fri Nov 07 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.6.0-4
- included docs, license and other missing files.

* Fri Nov 07 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.6.0-3
- consistent use of macros - replaced %%{buildroot} with $RPM_BUILD_ROOT

* Thu Nov 06 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.6.0-2
- Cleaned up buildrequire

* Tue Nov 04 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.6.0-1
- initial package
