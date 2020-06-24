Name:           nanomsg
Summary:        Socket library that provides several common communication patterns
Version:        1.1.5
Release:        3%{?dist}
License:        MIT
URL:            https://nanomsg.org/
Source0:        https://github.com/nanomsg/nanomsg/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
# For docs only, can be skipped
BuildRequires:  rubygem-asciidoctor

%description
The nanomsg library is a simple high-performance implementation of several
"scalability protocols". These scalability protocols are light-weight messaging
protocols which can be used to solve a number of very common messaging patterns,
such as request/reply, publish/subscribe, surveyor/respondent, and so forth.
These protocols can run over a variety of transports such as TCP, UNIX sockets,
and even WebSocket.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    doc
This package contains documentation for %{name}.


%prep
%setup -q

%build
%cmake -DTHREADSAFE=ON .
%make_build

%install
%make_install

%check
ctest .


%files
%license COPYING
%{_bindir}/nanocat
%{_libdir}/libnanomsg.so.5*
%{_mandir}/man1/*.1*

%files devel
%doc tests
%{_libdir}/libnanomsg.so
%{_libdir}/pkgconfig/nanomsg.pc
%{_libdir}/cmake/nanomsg-%{version}/
%{_includedir}/nanomsg/
%{_defaultdocdir}/nanomsg/
%{_mandir}/man3/*.3*
%{_mandir}/man7/*.7*

%files doc
%doc AUTHORS doc README.md RELEASING SUPPORT

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Troy Dawson <tdawson@redhat.com> - 1.1.5-1
- Initial package
