# Generated by rust2rpm 10
%bcond_without check
%global __cargo_skip_build 0

Name:           mirrorlist-server
Version:        3.0.1
Release:        1%{?dist}
Summary:        Mirrorlist Server

# Upstream license specification: MIT
# ASL 2.0
# ISC
# MIT
# MIT or ASL 2.0
# Unlicense or MIT
License:        MIT and ASL 2.0 and ISC
URL:            https://github.com/adrianreber/mirrorlist-server
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
The mirrorlist-server uses the data created by `MirrorManager2
<https://github.com/fedora-infra/mirrormanager2>`_ to answer client request for
the "best" mirror.

This implementation of the mirrorlist-server is written in Rust. The original
version of the mirrorlist-server was part of the MirrorManager2 repository and
it is implemented using Python. While moving from Python2 to Python3 one of
the problems was that the data exchange format (Python Pickle) did not support
running the MirrorManager2 backend with Python2 and the mirrorlist frontend
with Python3. To have a Pickle independent data exchange format protobuf was
introduced. The first try to use protobuf in the python mirrorlist
implementation required a lot more memory than the Pickle based implementation
(3.5GB instead of 1.1GB). That is one of the reasons a new mirrorlist-server
implementation was needed.

Another reason to rewrite the mirrorlist-server is its architecture. The
Python based version requires the Apache HTTP server or something that can
run the included wsgi. The wsgi talks over a socket to the actual
mirrorlist-server. In Fedora's MirrorManager2 instance this runs in a container
which runs behind HAProxy. This implementation in Rust directly uses a HTTP
library to reduce the number of involved components.

In addition to being simpler this implementation also requires less memory
than the Python version.}

%description %{_description}

%files
%license LICENSE
%doc README.rst
%{_bindir}/mirrorlist-server
%{_bindir}/generate-mirrorlist-cache

%prep
%autosetup -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# Upstream is working on fixing this
%cargo_test -- --bin mirrorlist-server
%endif

%changelog
* Thu Jun 18 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1

* Wed Jun 17 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0

* Wed Jun 17 2020 Adrian Reber <adrian@lisas.de> - 2.3.0-2
- Include patch from upstream to fix #1844087

* Mon May 11 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Fri Mar 27 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Mon Mar 23 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 09:11:47 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Initial package