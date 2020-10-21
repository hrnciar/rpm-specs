%bcond_without check

%global _hardened_build 1

# https://github.com/shuLhan/go-bindata
%global goipath         github.com/shuLhan/go-bindata
Version:                3.6.1

%gometa

%global common_description %{expand:
A small utility which generates Go code from any file. Useful for embedding
binary data in a Go program.}

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTING.md README.md CHANGELOG

Name:           %{goname}
Release:        1%{?dist}
Summary:        A small utility which generates Go code from any file

# Upstream license specification: CC0-1.0
License:        CC0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  help2man

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/go-bindata.shulhan %{goipath}/cmd/go-bindata
mkdir -p %{gobuilddir}/share/man/man1
help2man --no-discard-stderr -n "%{summary}" -s 1 -o %{gobuilddir}/share/man/man1/go-bindata.shulhan.1 -N --version-string="%{version}" %{gobuilddir}/bin/go-bindata.shulhan

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                                %{buildroot}%{_mandir}/man1
install -m 0644 -vp %{gobuilddir}/share/man/man1/* %{buildroot}%{_mandir}/man1/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc AUTHORS CONTRIBUTING.md README.md CHANGELOG
%{_mandir}/man1/go-bindata.shulhan.1*
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Aug 31 2020 Brandon Perkins <bperkins@redhat.com> - 3.6.1-1
- Update to version 3.6.1 (#1874216)

* Mon Aug 03 2020 Brandon Perkins <bperkins@redhat.com> - 3.6.0-2
- Rename binary to go-bindata.shulhan so it does not conflict with go-bindata

* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 3.6.0-1
- Initial package (#1862861)
