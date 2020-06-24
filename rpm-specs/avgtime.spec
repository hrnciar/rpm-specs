# This is the date of the latest upstream git commit.
%global verdate 20150501

Name:           avgtime
Version:        0.5.1
Release:        0.24.git%{verdate}%{?dist}
Summary:        Time a command and print average, standard deviation

License:        Boost
URL:            https://github.com/jmcabo/avgtime

# There are no upstream source tarballs.  The source tarball
# here was constructed as follows:
#
#   git clone https://github.com/jmcabo/avgtime.git
#   cd avgtime
#   d=YYYYMMDD  # date of latest upstream git commit
#   git archive -o /tmp/avgtime-$d.tar.gz --prefix=avgtime-$d/ HEAD
#
Source0:        avgtime-%{verdate}.tar.gz

ExclusiveArch:  %{ldc_arches}

BuildRequires:  ldc
BuildRequires:  ldc-druntime
BuildRequires:  ldc-phobos-devel


%description
'avgtime' works like the Linux 'time' command, except it runs the
command repeatedly and displays statistics:

- median
- average
- standard deviation
- 95% and 99% confidence intervals


%prep
%setup -q -n avgtime-%{verdate}


%build
ldc2 %{_d_optflags} avgtime.d


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -a avgtime $RPM_BUILD_ROOT%{_bindir}


%files
%license LICENSE_1_0.txt
%doc README.md
%{_bindir}/avgtime


%changelog
* Mon Feb 10 2020 Kalev Lember <klember@redhat.com> - 0.5.1-0.24.git20150501
- Rebuilt for ldc 1.20

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.23.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.22.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 09 2019 Kalev Lember <klember@redhat.com> - 0.5.1-0.21.git20150501
- Rebuilt for ldc 1.15

* Mon Feb 18 2019 Kalev Lember <klember@redhat.com> - 0.5.1-0.20.git20150501
- Rebuilt for ldc 1.14

* Wed Feb 06 2019 Richard W.M. Jones <rjones@redhat.com> - 0.5.1-0.19.git20150501
- Bump release and rebuild against latest ldc.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.18.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 14 2018 Kalev Lember <klember@redhat.com> - 0.5.1-0.17.git20150501
- Rebuilt for ldc 1.12

* Tue Aug 21 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.1-0.16.git20150501
- Use %%license
- Rebuild for aarch64

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.5.1-0.15.git20150501
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.14.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Kalev Lember <klember@redhat.com> - 0.5.1-0.13.git20150501
- Rebuilt for ldc 1.11

* Mon Feb 19 2018 Kalev Lember <klember@redhat.com> - 0.5.1-0.12.git20150501
- Rebuilt for ldc 1.8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.11.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 0.5.1-0.10.git20150501
- Rebuilt for ldc 1.4

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.9.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.8.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Kalev Lember <klember@redhat.com> - 0.5.1-0.7.git20150501
- Rebuilt for new ldc compiler

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.6.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Richard W.M. Jones <rjones@redhat.com> - 0.5.1-0.5.git20150501
- Bump and rebuild for new compiler.

* Sun Oct 30 2016 Kalev Lember <klember@redhat.com> - 0.5.1-0.4.git20150501
- Use new ldc_arches macro

* Mon Oct 24 2016 Kalev Lember <klember@redhat.com> - 0.5.1-0.3.git20150501
- Enable arm and i686 architectures now that ldc is available there

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-0.2.git20150501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Richard W.M. Jones <rjones@redhat.com> - 0.5.1-0.1.git20150501
- Rebuild for latest D incompatibility.
- Update to latest git version.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.15.git20141110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 02 2015 Richard W.M. Jones <rjones@redhat.com> - 0-0.14.git20141110
- Bump to fix latest D library brokenness.
- Disable 32 bit x86 which is broken.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.12.git20130201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.git20130201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Richard W.M. Jones <rjones@redhat.com> - 0-0.10.git20130201
- Bump again to try to fix latest D library brokenness.

* Sat Aug  3 2013 Richard W.M. Jones <rjones@redhat.com> - 0-0.9.git20130201
- ExcludeArch armv7hl.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git20130201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul  7 2013 Richard W.M. Jones <rjones@redhat.com> - 0-0.7.git20130201
- Bump yet again to try to fix latest D library brokenness.

* Mon Jun 17 2013 Richard W.M. Jones <rjones@redhat.com> - 0-0.6.git20130201
- Move to latest upstream git.
- Bump and rebuild again to fix broken dependency.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git20120724
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 10 2012 Richard W.M. Jones <rjones@redhat.com> - 0-0.4.git20120724
- Try bump and rebuild again to fix broken dependency.

* Thu Sep 27 2012 Richard W.M. Jones <rjones@redhat.com> - 0-0.3.git20120724
- Bump and rebuild.

* Thu Jul 26 2012 Richard W.M. Jones <rjones@redhat.com> - 0-0.2.git20120724
- Rebuild against fixed ldc.
- Add _d_optflags (thanks Jonathan Mercier).

* Wed Jul 25 2012 Richard W.M. Jones <rjones@redhat.com> - 0-0.1.git20120724
- Initial release.
