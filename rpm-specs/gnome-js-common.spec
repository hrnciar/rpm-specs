%global major_ver 0.1

Name:           gnome-js-common
Version:        %{major_ver}.2
Release:        20%{?dist}
Summary:        Common modules for GNOME JavaScript interpreters

# LGPLv3 part still being clarified with upstream
License:        BSD and MIT and LGPLv3
URL:            http://ftp.gnome.org/pub/GNOME/sources/%{name}
Source0:        ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{major_ver}/%{name}-%{version}.tar.bz2
# http://git.gnome.org/browse/gnome-js-common/patch/?id=d6ba3133f44ec888af8d64c87822d1bff7c891fe
Patch0:         %{name}-0.1.2-license.patch

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  intltool

%description
This package contains some JavaScript modules for use by GNOME
JavaScript extensions, namely GJS and Seed.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1 -b .license


%build
# not using standard configure macro. Nothing is compiled,
# make libdir point to %%{_datadir}
%configure --prefix=%{_prefix} --libdir=%{_datadir}
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"


%files
%doc COPYING ChangeLog
%{_datadir}/gnome-js
%exclude %{_docdir}/gnome_js_common

%files devel
%{_datadir}/pkgconfig/gnome-js-common.pc


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Jaromir Capik <jcapik@redhat.com> - 0.1.2-10
- Last time I forgot to replace the ./configure call with the macro (#1071043)

* Tue May 13 2014 Jaromir Capik <jcapik@redhat.com> - 0.1.2-9
- Fixing FTBFS on ppc64le (#1071043)
- Cleaning the spec

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jun 17 2010 Michel Salim <salimma@fedoraproject.org> - 0.1.2-3
- Drop buildroot
- Specify patch version manually; Emacs rpm-spec mode gets confused if this
  is done via macros

* Fri Jun 11 2010 Michel Alexandre Salim <michel@hypatia.localdomain> - 0.1.2-2
- Review feedback:
- Drop noarch patch; point libdir to %%{_datadir} instead
- Drop %%clean section; not needed on F-13+

* Mon Mar 29 2010 Michel Salim <salimma@fedoraproject.org> - 0.1.2-1
- Initial package

