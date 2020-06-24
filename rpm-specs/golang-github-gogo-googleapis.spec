# Generated by go2rpm
%bcond_without check

# https://github.com/gogo/googleapis
%global goipath         github.com/gogo/googleapis
Version:                1.2.0

%gometa

%global common_description %{expand:
Google APIs generated by gogoprotobuf.}

%global golicenses      LICENSE
%global godocs          Readme.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Google APIs generated by gogoprotobuf

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/protoc-gen-gogo/descriptor)
BuildRequires:  golang(github.com/gogo/protobuf/types)
BuildRequires:  golang(github.com/gogo/protobuf/vanity)
BuildRequires:  golang(github.com/gogo/protobuf/vanity/command)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in protoc-gen-gogogoogleapis; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc Readme.md
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 04 17:04:20 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-1
- Initial package