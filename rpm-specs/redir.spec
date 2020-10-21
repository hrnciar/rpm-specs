Name:           redir
Version:        2.2.1
Release:        25%{?dist}
Summary:        Redirect TCP connections

License:        GPL+
URL:            http://sammy.net/~sammy/hacks/
Source0:        http://sammy.net/~sammy/hacks/%{name}-%{version}.tar.gz

BuildRequires: gcc

#Include Debian Patches
Patch0:         01_fix_max_bandwidth_docs.dpatch
Patch1:         02_use_ntohs.dpatch
Patch2:         03_fix_tcp_wrappers.dpatch
Patch3:         04_fix_timeouts.dpatch
Patch4:         05_pedantic.dpatch
Patch5:         06_fix_shaper_buffer.dpatch
Patch6:         07_cosmetics.dpatch
Patch7:         08_add_wrappers.dpatch
Patch8:         09_add_linux_software_map.dpatch
Patch9:         15_deb_cosmetics.dpatch
Patch10:        20_do_not_strip.dpatch
Patch11:        25_fix_setsockopt.dpatch
Patch12:        30_fix_manpage.dpatch
#end of debian patches

Patch13:        redir_gcc4.4-signedness.patch
Patch14:        31_fix_transproxy_location.patch
%description
a port redirector, used to forward incoming connections to somewhere else.
by far the cleanest piece of code here, because someone else liked it
enough to fix it.

%prep
%setup -q

# Fix docs and --help to show --max_bandwidth instead of --maxbandwidth
%patch0 -p1

#use ntohs() to generate comprehensible debug()s and syslog()s
%patch1 -p1

#fix calls to tcp wrappers
%patch2 -p1

# fix and make timeout more verbose
%patch3 -p1

#changes to make clean up compilation, include missing time.h include
%patch4 -p1

#properly allocate copyloop buffer
%patch5 -p1

#cosmestic only patch
%patch6 -p1

#add tcp_wrapper support
# %patch7 -p1

#description of redir
%patch8 -p1

#comestic only patch
%patch9 -p1

# do not stripping needed for debug-info package
%patch10 -p1

#make usage os setsockopt more verbose
%patch11 -p1

#Clean up questionable formatting in man page
%patch12 -p1

#fix compile warning with gcc 4.4
%patch13 -p2

# fix location of transproxy.txt
%patch14 -p2

# Convert to utf-8
for file in CHANGES; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
done

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -Dp -m 755 %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}
install -Dp -m 644 %{name}.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1



%files
%doc README CHANGES COPYING trans*.txt
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.2.1-20
- add gcc into buildrequires
- disable tcp_wrappers

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 10 2010 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.2.1-6
- fix building for EL-6

* Fri Sep 25 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.2.1-5
- start building for EPEL

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 04 2009 Itamar Reis Peixoto - 2.2.1-3
- fix compile warning with gcc 4.4
- include README and COPYING into %%doc section
- remove attr from files section
- convert CHANGES TO utf-8
- fix location of transproxy.txt file in manpage

* Wed Apr 01 2009 Itamar Reis Peixoto - 2.2.1-2
- Include Debian Patches

* Tue Mar 31 2009 Itamar Reis Peixoto - 2.2.1-1
- Initial RPM version
