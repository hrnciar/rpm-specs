%global git_date 20200421

Summary:	Parallel LZMA compressor using XZ
Name:		pxz
Version:	4.999.9
Release:	20.beta.%{git_date}git%{?dist}
License:	GPLv2+
URL:		https://jnovy.fedorapeople.org/pxz/
# source created as "make dist" in checked out GIT tree: git clone git://github.com/jnovy/pxz.git
Source0:	https://jnovy.fedorapeople.org/%{name}/%{name}-%{version}beta.%{git_date}git.tar.xz
Patch0:		pxz-4.999.9-cve-2015-1200.patch
Patch1:		pxz-4.999.9-revert-fa3194e.patch
BuildRequires:	gcc, xz-devel

%description
Parallel XZ is a compression utility that takes advantage of running
XZ compression simultaneously on different parts of an input file on
multiple cores and processors. This significantly speeds up compression
time.

%prep
%setup -q -n %{name}-%{version}beta
%patch0 -p1 -b .cve-2015-1200
%patch1 -p1 -b .revert-fa3194e

%build
export CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE"
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.999.9-20.beta.20200421git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Robert Scheck <robert@fedoraproject.org> 4.999.9-19.beta.20200421git
- Update to GIT 20200421
- Added patch against race condition in setting permissions on output file (#1182024)
- Added patch to revert environment redirect allowing 'export XZ_OPT="-9"' or similar

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.999.9-18.beta.20120930git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.999.9-17.beta.20120930git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.999.9-16.beta.20120930git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.999.9-15.beta.20120930git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.999.9-14.beta.20120930git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.999.9-13.beta.20120930git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.999.9-12.beta.20120930git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.999.9-11.beta.20120930git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.999.9-10.beta.20120930git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.999.9-9.beta.20120930git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.999.9-8.beta.20120930git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.999.9-7.beta.20120930git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.999.9-6.beta.20120930git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.999.9-5.beta.20120930git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 30 2012 Jindrich Novy <jnovy@redhat.com> 4.999.9-1.beta.20120930git
- sync with upstream

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.999.9-4.beta.20100608git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.999.9-3.beta.20100608git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.999.9-2.beta.20100608git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun  8 2010 Jindrich Novy <jnovy@redhat.com> 4.999.9-1.beta.20100608git
- initial import release

* Thu Jun  3 2010 Jindrich Novy <jnovy@redhat.com> 4.999.9-0.1.beta.20100603git
- review fixes (#598902)

* Wed May 26 2010 Jindrich Novy <jnovy@redhat.com> 4.999.9-0.1.beta.20100526git
- add -D option to specify context size per thread

* Fri Feb 19 2010 Jindrich Novy <jnovy@redhat.com> 4.999.9-0.1.beta.20100217git
- better error handling and stability fixes

* Wed Dec  9 2009 Jindrich Novy <jnovy@redhat.com> 4.999.9-0.1.beta.20091209git
- use fixed size context per thread (3x dict size by default)
- reduce memory requirements for compression

* Wed Nov 18 2009 Jindrich Novy <jnovy@redhat.com> 4.999.9-0.1.beta.20091118git
- initial packaging
