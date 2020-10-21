%bcond_without check

%global _hardened_build 1

# https://github.com/aliyun/ossutil
%global goipath         github.com/aliyun/ossutil
Version:                1.6.19
%global tag             1.6.19

%gometa

%global common_description %{expand:
Alibaba Cloud (Aliyun) Object Storage Service (OSS) CLI.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README-CN.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Alibaba Cloud (Aliyun) Object Storage Service (OSS) CLI

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/aliyun/aliyun-oss-go-sdk/oss)
BuildRequires:  golang(github.com/alyu/configparser)
BuildRequires:  golang(github.com/droundy/goopt)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb)
BuildRequires:  help2man

%if %{with check}
# Tests
BuildRequires:  golang(gopkg.in/check.v1)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/ossutil %{goipath}
mkdir -p %{gobuilddir}/share/man/man1
help2man --no-discard-stderr -n "%{summary}" -s 1 -o %{gobuilddir}/share/man/man1/ossutil.1 -N --version-string="%{version}" %{gobuilddir}/bin/ossutil

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                                %{buildroot}%{_mandir}/man1
install -m 0644 -vp %{gobuilddir}/share/man/man1/* %{buildroot}%{_mandir}/man1/

%if %{with check}
%check
# Skip 'lib' tests due to need for credentials
%gocheck -d 'lib'
%endif

%files
%license LICENSE
%doc CHANGELOG.md README-CN.md README.md
%{_mandir}/man1/ossutil.1*
%{_bindir}/*

%gopkgfiles

%changelog
* Fri Sep 04 2020 Brandon Perkins <bperkins@redhat.com> - 1.6.19-1
- Update to version 1.6.19 (#1875619)

* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 1.6.18-3
- Update summary and description for clarity and consistency

* Wed Jul 29 2020 Brandon Perkins <bperkins@redhat.com> - 1.6.18-2
- Enable check stage
- Disable 'lib' tests due to need for credentials
- Add version tag
- Remove explicit gzip of man page

* Tue Jul 28 2020 Brandon Perkins <bperkins@redhat.com> - 1.6.18-1
- Update to version 1.6.18 (#1811182)
- Explicitly harden package
- Remove golang(github.com/satori/go.uuid)
  (commit=b2ce2384e17bbe0c6d34077efa39dbab3e09123b) BuildRequires
- Fix man page generation
- Clean changelog

* Fri Mar 06 2020 Brandon Perkins <bperkins@redhat.com> - 1.6.10-2
- Add man page

* Wed Mar 04 2020 Brandon Perkins <bperkins@redhat.com> - 1.6.10-1
- Update to version 1.6.10

* Fri Nov 22 2019 Brandon Perkins <bperkins@redhat.com> - 1.6.9-1
- Initial package

