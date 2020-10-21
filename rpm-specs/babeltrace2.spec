Name:           babeltrace2
Version:        2.0.3
Release:        3%{?dist}
Summary:        A trace manipulation toolkit
# # For a breakdown of the licensing, see LICENSE
License:        MIT and GPLv2
URL:            https://www.efficios.com/babeltrace
Source0:        https://www.efficios.com/files/babeltrace/babeltrace2-%{version}.tar.bz2
Source1:        https://www.efficios.com/files/babeltrace/babeltrace2-%{version}.tar.bz2.asc
# gpg2 --export --export-options export-minimal 7F49314A26E0DE78427680E05F1B2A0789F12B11 > gpgkey-7F49314A26E0DE78427680E05F1B2A0789F12B11.gpg
Source2:        gpgkey-7F49314A26E0DE78427680E05F1B2A0789F12B11.gpg

BuildRequires:  autoconf >= 2.50
BuildRequires:  automake >= 1.10
BuildRequires:  bison >= 2.4
BuildRequires:  elfutils-devel >= 0.154
BuildRequires:  flex >= 2.5.35
BuildRequires:  glib2-devel >= 2.28.0
BuildRequires:  gnupg2
BuildRequires:  libtool >= 2.2
BuildRequires:  python3-devel >= 3.4
BuildRequires:  swig >= 3.0

Requires:       libbabeltrace2%{?_isa} = %{version}-%{release}

%description
The Babeltrace 2 project offers a library with a C API, Python 3 bindings, and
a command-line tool which makes it very easy for mere mortals to view,
convert, transform, and analyze traces.

Babeltrace 2 is also the reference parser implementation of the Common Trace
Format (CTF), a very versatile trace format followed by various tracers and
tools such as LTTng and barectf.


%package -n libbabeltrace2
Summary:        A trace manipulation library

%description -n libbabeltrace2
The libbabeltrace2 package contains a library and plugin system to view,
convert, transform, and analyze traces.


%package -n libbabeltrace2-devel
Summary:        Development files for libbabeltrace2
Requires:       libbabeltrace2%{?_isa} = %{version}-%{release} glib2-devel

%description -n libbabeltrace2-devel
The libbabeltrace2-devel package contains the header files and libraries
needed to develop programs that use the libbabeltrace2 trace manipulation
library.


%package -n python3-bt2
Summary:        libbabeltrace2 Python bindings
Requires:       libbabeltrace2%{?_isa} = %{version}-%{release}

%description -n python3-bt2
The python3-bt2 package provides Python 3 bindings for libbabeltrace2.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
# Reinitialize libtool with the fedora version to remove Rpath
autoreconf -vif

export PYTHON=%{__python3}
export PYTHON_CONFIG=%{__python3}-config
%configure --disable-static \
	--enable-python-bindings \
	--enable-python-plugins \
	--enable-debug-info \
	--disable-Werror

make %{?_smp_mflags} V=1

%check
make check

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete
# Clean installed doc
rm -f %{buildroot}/%{_pkgdocdir}/CONTRIBUTING.adoc
rm -f %{buildroot}/%{_pkgdocdir}/LICENSE
rm -f %{buildroot}/%{_pkgdocdir}/gpl-2.0.txt
rm -f %{buildroot}/%{_pkgdocdir}/lgpl-2.1.txt
rm -f %{buildroot}/%{_pkgdocdir}/mit-license.txt
rm -f %{buildroot}/%{_pkgdocdir}/std-ext-lib.txt

%ldconfig_scriptlets  -n lib%{name}

%files
%doc ChangeLog
%doc README.adoc
%{!?_licensedir:%global license %%doc}
%license LICENSE gpl-2.0.txt mit-license.txt
%{_bindir}/babeltrace2
%{_mandir}/man1/*.1*
%{_mandir}/man7/*.7*

%files -n libbabeltrace2
%{!?_licensedir:%global license %%doc}
%license LICENSE gpl-2.0.txt mit-license.txt
%{_libdir}/*.so.*
%{_libdir}/babeltrace2/plugin-providers/*.so
%{_libdir}/babeltrace2/plugins/*.so

%files -n libbabeltrace2-devel
%{_prefix}/include/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/babeltrace2.pc
%{_libdir}/pkgconfig/babeltrace2-ctf-writer.pc

%files -n python3-bt2
%{python3_sitearch}/bt2
%{python3_sitearch}/bt2*.egg-info


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-2
- Rebuilt for Python 3.9

* Fri Apr 24 2020 Michael Jeanson <mjeanson@efficios.com> - 2.0.3-1
- New upstream release

* Thu Mar 12 2020 Michael Jeanson <mjeanson@efficios.com> - 2.0.2-1
- New upstream release

* Mon Feb 10 2020 Michael Jeanson <mjeanson@efficios.com> - 2.0.1-1
- New upstream release
