# TODO: if built as PIE, fails with "read: Bad address"
#global _hardened_build 1

Name:           seeker
Version:        3.0
Release:        21%{?dist}
Summary:        Random access disk benchmark utility

License:        GPLv2 and CC-BY-SA
URL:            http://www.linuxinsight.com/how_fast_is_your_disk.html
# http://www.linuxinsight.com/how_fast_is_your_disk.html#comment-1583
Source0:        http://smp.if.uj.edu.pl/~baryluk/seeker_baryluk.c
# http://www.linuxinsight.com/how_fast_is_your_disk.html?page=1#comment-971
Source1:        %{name}.LICENSE
# Grabbed with firefox, modified, ran through tidy(1) per CC BY-SA 2.5:
# http://www.linuxinsight.com/about.html
Source2:        %{name}-docs.tar.gz
# https://bugzilla.redhat.com/623667
Patch0:         %{name}-3.0-timeout-blockalign-623667.patch

BuildRequires:  gcc
%description
Seeker is a simple utility that reads small pieces of data from a raw
disk device in a random access pattern, and reports the average number
of seeks per second, and calculated random access time of the disk.
The seeker variant included in this package is the multithreaded one
by Witold Baryluk.


%prep
%setup -q -c -T -a 2
install -pm 644 %{SOURCE0} $(basename %{SOURCE0}) # for debuginfo, Patch0
%patch0
cp -p %{SOURCE1} LICENSE


%build
%{__cc} -D_GNU_SOURCE $RPM_OPT_FLAGS $RPM_LD_FLAGS -pthread \
    $(basename %{SOURCE0}) -o seeker


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 seeker $RPM_BUILD_ROOT%{_sbindir}/seeker



%files
%doc LICENSE how_fast_is_your_disk*
%{_sbindir}/seeker


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Ville Skyttä <ville.skytta@iki.fi> - 3.0-6
- Build with $RPM_LD_FLAGS.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 19 2010 Ville Skyttä <ville.skytta@iki.fi> - 3.0-3
- Apply Ian Sherratt's (modified) timeout/block-alignment patch (#623667).

* Sun Sep 13 2009 Ville Skyttä <ville.skytta@iki.fi> - 3.0-2
- Address review comments (#520701):
- Improve %%description.
- Include upstream article in docs.

* Fri Aug 28 2009 Ville Skyttä <ville.skytta@iki.fi> - 3.0-1
- First build.
