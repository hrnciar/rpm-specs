%global git_commit 4f795aeba2d9ee52f82e8666d55f6a469576dfa0
%global git_date 20200903

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Summary:  Timezone information for the Cyrus IMAP Server
Name: cyrus-timezones
Version:  %{git_date}
Release: 1.%{git_suffix}%{dist}
License: GPLv2+
Group: Applications/Internet
URL: https://github.com/cyrusimap/cyrus-timezones
Source0: https://github.com/cyrusimap/%{name}/archive/%{git_commit}/%{name}-%{version}.tar.gz

BuildRequires: autoconf, automake, libtool
BuildRequires: libical-devel
BuildRequires: glib2-devel
BuildRequires: chrpath

%description
%{summary}

%package devel
Summary: Package config configuration for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconf-pkg-config

%description devel
%{summary}

%prep
%autosetup -p1 -n %{name}-%{git_commit}
autoreconf -i --verbose  --warnings=all

%build
%configure
%make_build

%install
%make_install 
chrpath -d %{buildroot}/%{_bindir}/cyr_vzic

%files
%doc AUTHORS README MAINTAINER_NOTES
%license COPYING
%{_datadir}/%{name}
%{_bindir}/cyr_vzic

%files devel
%{_libdir}/pkgconfig/%{name}.pc

%changelog

* Thu Sep 03 2020  Pavel Zhukov <pzhukov@redhat.com> - 20200903-1.20200903git4f795aeb
- Do not use deprecated macroses

* Mon Aug 31 2020 Pavel Zhukov <pzhukov@redhat,com> - 20200901-2.20200901git8c24df1d
- Initial build.
- Fix changelog entry format. 

