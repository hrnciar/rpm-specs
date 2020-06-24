# Generated by go2rpm
%ifnarch s390x
%bcond_without check
%endif

# https://github.com/influxdata/flux
%global goipath         github.com/influxdata/flux
Version:                0.65.0

%gometa

%global common_description %{expand:
Flux is a lightweight scripting language for querying databases (like influxdb)
and working with data. it's part of influxdb 1.7 and 2.0, but can be run
independently of those.}

%global golicenses      LICENSE
%global godocs          docs examples CONTRIBUTING.md README.md

%global gosupfiles      "${flux[@]}" stdlib/testing/testdata/* stdlib/pandas_tests/testdata/* stdlib/strings/testdata/*

Name:           %{goname}
Release:        1%{?dist}
Summary:        Lightweight scripting language for querying databases

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(cloud.google.com/go/bigtable)
BuildRequires:  golang(github.com/andreyvit/diff)
BuildRequires:  golang(github.com/apache/arrow/go/arrow)
BuildRequires:  golang(github.com/apache/arrow/go/arrow/array)
BuildRequires:  golang(github.com/apache/arrow/go/arrow/bitutil)
BuildRequires:  golang(github.com/apache/arrow/go/arrow/math)
BuildRequires:  golang(github.com/apache/arrow/go/arrow/memory)
# BuildRequires:  golang(github.com/benbjohnson/tmpl)
BuildRequires:  golang(github.com/c-bata/go-prompt)
BuildRequires:  golang(github.com/cespare/xxhash)
BuildRequires:  golang(github.com/dave/jennifer/jen)
BuildRequires:  golang(github.com/eclipse/paho.mqtt.golang)
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/golang/geo/r1)
BuildRequires:  golang(github.com/golang/geo/s1)
BuildRequires:  golang(github.com/golang/geo/s2)
BuildRequires:  golang(github.com/google/flatbuffers/go)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
# BuildRequires:  golang(github.com/goreleaser/goreleaser)
# BuildRequires:  golang(github.com/influxdata/changelog)
BuildRequires:  golang(github.com/influxdata/line-protocol)
BuildRequires:  golang(github.com/influxdata/promql)
BuildRequires:  golang(github.com/influxdata/promql/pkg/labels)
BuildRequires:  golang(github.com/influxdata/tdigest)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/mattn/go-sqlite3)
BuildRequires:  golang(github.com/matttproud/golang_protobuf_extensions/pbutil)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/log)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/prometheus/client_model/go)
BuildRequires:  golang(github.com/prometheus/common/expfmt)
BuildRequires:  golang(github.com/prometheus/common/model)
BuildRequires:  golang(github.com/satori/go.uuid)
BuildRequires:  golang(github.com/segmentio/kafka-go)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(go.uber.org/zap)
BuildRequires:  golang(go.uber.org/zap/zapcore)
BuildRequires:  golang(go.uber.org/zap/zaptest)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/tools/go/packages)
BuildRequires:  golang(gonum.org/v1/gonum/floats)
BuildRequires:  golang(google.golang.org/api/option)
# BuildRequires:  golang(honnef.co/go/tools/cmd/staticcheck)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/DATA-DOG/go-sqlmock)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
rm -rf internal/tools
mapfile -t flux <<< $(find . -iname "*.flux" -type f)
sed -i "s|github.com/influxdata/promql/v2|github.com/influxdata/promql|" $(find . -iname "*.go")

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck -t stdlib \
         -d execute
%endif

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*

%gopkgfiles

%changelog
* Sat Apr 04 21:27:23 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.65.0-1
- Update to 0.65.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 16:55:33 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.37.2-3
- Force inclusion of stdlib/strings/testdata/

* Mon Aug 05 16:55:33 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.37.2-2
- Force inclusion of stdlib/pandas_tests/testdata

* Mon Aug 05 15:32:29 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.37.2-1
- Release 0.37.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 22:46:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.28.0-1
- Initial package
