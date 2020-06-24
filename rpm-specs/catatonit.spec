%define built_tag v0.1.5
%define built_tag_strip %(b=%{built_tag}; echo ${b:1})
%define download_url %{url}/archive/%{built_tag}.tar.gz

Name: catatonit
Version: 0.1.5
Release: 2%{?dist}
Summary: A signal-forwarding process manager for containers
License: GPLv3+
URL: https://github.com/openSUSE/catatonit
Source0: %{download_url}
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: file
BuildRequires: gcc
BuildRequires: git
BuildRequires: glibc-static
BuildRequires: libtool

%description
Catatonit is a /sbin/init program for use within containers. It
forwards (almost) all signals to the spawned child, tears down
the container when the spawned child exits, and otherwise
cleans up other exited processes (zombies).

This is a reimplementation of other container init programs (such as
"tini" or "dumb-init"), but uses modern Linux facilities (such as
signalfd(2)) and has no additional features.

%prep
%autosetup -Sgit -n %{name}-%{built_tag_strip}

%build
autoreconf -fi
%configure
%{__make} %{?_smp_mflags}

# Make sure we *always* build a static binary. Otherwise we'll break containers
# that don't have the necessary shared libs.
file ./%{name} | grep 'statically linked'
if [ $? != 0 ]; then
   echo "ERROR: %{name} binary must be statically linked!"
   exit 1
fi

%install
install -dp %{buildroot}%{_libexecdir}/%{name}
install -p %{name} %{buildroot}%{_libexecdir}/%{name}
install -dp %{buildroot}%{_libexecdir}/podman
ln -s %{_libexecdir}/%{name}/%{name} %{buildroot}%{_libexecdir}/podman/%{name}

%files
%license COPYING
%doc README.md
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/%{name}

%changelog
* Wed Apr 29 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1.5-2
- complain if not statically linked, patch from Jindrich Novy <jnovy@redhat.com> 

* Wed Apr 29 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1.5-1
- bump to v0.1.5
- static binary to not break containers that don't have necessary shared libs

* Wed Feb 19 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1.4-1
- first build for review
- source copied from openSUSE @ https://build.opensuse.org/package/show/openSUSE:Factory/catatonit
