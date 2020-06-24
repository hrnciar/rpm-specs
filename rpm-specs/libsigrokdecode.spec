Name:           libsigrokdecode
Version:        0.5.3
Release:        3%{?dist}
Summary:        Basic API for running protocol decoders
# Combined GPLv3+ and GPLv2+
License:        GPLv3+
URL:            http://www.sigrok.org
Source0:        %{url}/download/source/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  python3-devel
BuildRequires:  doxygen
BuildRequires:  graphviz

%description
%{name} is a shared library written in C which provides the basic API
for running sigrok protocol decoders. The protocol decoders themselves
are written in Python.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for developing software
using %{name}.

%prep
%setup -q

# Bytecompile script yet again wants to break our build. Retarded!
%global _python_bytecompile_errors_terminate_build 0

%build
%configure --disable-static
V=1 make %{?_smp_mflags}

# This builds documentation for the -doc package
doxygen Doxyfile


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets


%files
%doc README NEWS COPYING
%{_libdir}/libsigrokdecode.so.4*
%{_datadir}/libsigrokdecode/


%files devel
%{_includedir}/libsigrokdecode/
%{_libdir}/libsigrokdecode.so
%{_libdir}/pkgconfig/libsigrokdecode.pc

%files doc
%doc doxy/html-api/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Dan Horák <dan[at]danny.cz> - 0.5.3-1
- updated to 0.5.3

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 mrnuke <mr.nuke.me@gmail.com> - 0.5.2-1
- New and exciting libsigrokdecode 0.5.2 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-5
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 14 2017 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.5.0-1
- Update to libsigrokdecode 0.5.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Dan Horák <dan[at]danny.cz> - 0.4.1-1
- updated to 0.4.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-1
- Rebuild for Python 3.6

* Sat Feb 06 2016 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.4.0-0
- Update to libsigrokdecode 0.4.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Jul 13 2015 Dan Horák <dan[at]danny.cz> - 0.3.1-1
- updated to 0.3.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 27 2014 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.3.0-1
- Update to libsigrokdecode-0.3.0 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
