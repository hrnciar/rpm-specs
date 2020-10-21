Name: kernelshark
Version: 1.2
Release: 1%{?dist}

# As of 1.1, only kernelshark.cpp, kshark-record.cpp and examples are GPL-2.0. The rest of kernel-shark is LGPL-2.1.
# See SPDX identifier for most accurate info
License: GPLv2 and LGPLv2
Summary: GUI analysis for Ftrace data captured by trace-cmd

URL: https://kernelshark.org
Source0: https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/snapshot/trace-cmd-kernelshark-v%{version}.tar.gz
Source1: %{name}.appdata.xml

Patch0: 0001-kernelshark-Temporary-move-libtraceevent-back-to-_li.patch
BuildRequires: cmake 
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: graphviz
BuildRequires: libappstream-glib
BuildRequires: pkgconf
BuildRequires: pkgconfig(glut)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(Qt5Core)
# Force dependency release < 20 so that when libtraceevent is out we can force an update by bumping trace-cmd version.
BuildRequires: trace-cmd-devel >= 2.9.1-3
BuildRequires: trace-cmd-devel < 2.9.1-20
BuildRequires: trace-cmd-libs  >= 2.9.1-3
BuildRequires: trace-cmd-libs  < 2.9.1-20
BuildRequires: xmlto
Requires: polkit


%description
KernelShark is a front end reader of trace-cmd output. "trace-cmd
record" and "trace-cmd extract" create a trace.dat (trace-cmd.dat)
file. kernelshark can read this file and produce a graph and list
view of its data. 

%prep
%setup -q -n trace-cmd-%{name}-v%{version}
%patch0 -p1
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1

%build
# MANPAGE_DOCBOOK_XSL define is hack to avoid using locate
# -z muldefs to workaround the enforcing multi definition check of gcc10.
#   and it need to be removed once upstream fixed the variable name
# Do not use parallel compile because it makes compiling fail
MANPAGE_DOCBOOK_XSL=`rpm -ql docbook-style-xsl | grep manpages/docbook.xsl`
CFLAGS="%{optflags} -D_GNU_SOURCE" LDFLAGS="%{build_ldflags} -z muldefs" BUILD_TYPE=Release \
  make -p V=9999999999 MANPAGE_DOCBOOK_XSL=$MANPAGE_DOCBOOK_XSL \
  prefix=%{_prefix} libdir=%{_libdir} gui

%install
make libdir=%{_libdir} prefix=%{_prefix} V=1 DESTDIR=%{buildroot}/ CFLAGS="%{optflags} -D_GNU_SOURCE" LDFLAGS="%{build_ldflags} -z muldefs " BUILD_TYPE=Release install_gui
find %{buildroot}%{_datadir} -type f | xargs chmod u-x,g-x,o-x
find %{buildroot}%{_libdir} -type f -iname "*.so" | xargs chmod 0755
sed -i '/Version/d' %{buildroot}/%{_datadir}/applications/kernelshark.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/kernelshark.desktop
mkdir -p %{buildroot}%{_metainfodir}/
cp %{SOURCE1} %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%license COPYING
%doc COPYING.LIB README
%{_bindir}/kernelshark
%{_bindir}/kshark-record
%{_bindir}/kshark-su-record
%dir %{_libdir}/kernelshark
%{_libdir}/kernelshark/*
%{_datadir}/applications/kernelshark.desktop
%dir %{_datadir}/icons/kernelshark
%{_datadir}/icons/kernelshark/*
%{_datadir}/polkit-1/actions/org.freedesktop.kshark-record.policy
%{_metainfodir}/%{name}.appdata.xml

%changelog
* Mon Oct 12 2020 Zamir SUN <sztsian@gmail.com> - 1.2-1
- Update to 1.2
- Uses trace event plugins from old trace-cmd dir

* Thu Sep 24 2020 Zamir SUN <sztsian@gmail.com> - 1.1-1
- Package kernelshark in a standalone package with 1.1

